import asyncio
import aiohttp
import async_timeout
from yarl import URL

from .const import API_HOST, AUTHENTICATION_PATH, SOURCES_PATH, AUTH_TOKEN_HEADER
from .exceptions import HuisbaasjeConnectionException, HuisbaasjeException


class Huisbaasje:
    """Client to connect with Huisbaasje"""

    def __init__(self, request_timeout: int = 10, source_types: list = []):
        self.request_timeout = request_timeout
        self.source_types = source_types

        self._user_id = None
        self._auth_token = None
        self._sources = None

    async def authenticate(self, username: str, password: str) -> None:
        """Log in using username and password"""
        url = URL.build(scheme="https", host=API_HOST, port=443, path=AUTHENTICATION_PATH)
        headers = {"Accept": "application/json"}
        data = {"loginName": username, "password": password}

        await self.request("POST", url, headers=headers, data=data, callback=self._handle_authenticate_response)

    async def _handle_authenticate_response(self, response):
        json = await response.json()
        self._auth_token = response.headers.get(AUTH_TOKEN_HEADER)
        self._user_id = json['userId']

    async def sources(self):
        url = URL.build(scheme="https", host=API_HOST, port=443, path=(SOURCES_PATH % self._user_id))
        headers = {
            "Accept": "application/json",
            AUTH_TOKEN_HEADER: self._auth_token
        }

        await self.request("GET", url, headers=headers, callback=self._handle_sources_response)

    async def _handle_sources_response(self, response):
        json = await response.json()
        self._sources = dict()
        for source in json['sources']:
            self._sources[source['type']] = source['source']

    async def actuals(self):
        pass

    async def request(self, method: str, url: str, headers: dict = None, data: dict = None, callback=None):
        try:
            with async_timeout.timeout(self.request_timeout):
                async with aiohttp.ClientSession() as session:
                    async with session.request(method, url, json=data, headers=headers, ssl=True) as response:
                        status = response.status
                        is_json = response.headers.get("Content-Type", "") == "application/json"

                        if not is_json or (status // 100) in [4, 5]:
                            raise HuisbaasjeException(response.status, await response.text())

                        if callback is not None:
                            await callback(response)

        except asyncio.TimeoutError as exception:
            raise HuisbaasjeConnectionException("Timeout occurred while communicating with Huisbaasje") from exception
        except aiohttp.ClientError as exception:
            raise HuisbaasjeConnectionException("Error occurred while communicating with Huisbaasje") from exception
