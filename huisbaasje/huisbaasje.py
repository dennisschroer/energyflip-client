import asyncio
import aiohttp
import async_timeout
from yarl import URL

from .const import API_HOST, AUTHENTICATION_PATH, SOURCES_PATH, AUTH_TOKEN_HEADER


class Huisbaasje:
    """Client to connect with Huisbaasje"""

    def __init__(self, request_timeout: int = 10):
        self.request_timeout = request_timeout

        # self._session = aiohttp.ClientSession()

        self.user_id = None
        self.auth_token = None
        self.sources = None

    async def authenticate(self, username: str, password: str) -> None:
        """Log in using username and password"""
        url = URL.build(scheme="https", host=API_HOST, port=443, path=AUTHENTICATION_PATH)

        headers = {
            "Accept": "application/json",
        }

        data = {
            "loginName": username,
            "password": password
        }

        try:
            with async_timeout.timeout(self.request_timeout):
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, json=data, headers=headers, ssl=True) as response:
                        # TODO better validation of response
                        json = await response.json()
                        self.auth_token = response.headers.get(AUTH_TOKEN_HEADER)
                        self.user_id = json['userId']

        except asyncio.TimeoutError as exception:
            # TODO better exception handling
            raise exception
        except (aiohttp.ClientError) as exception:
            # TODO better exception handling
            raise exception

    async def sources(self):
        url = URL.build(scheme="https", host=API_HOST, port=443, path=(SOURCES_PATH % self.user_id))

        headers = {
            "Accept": "application/json",
            AUTH_TOKEN_HEADER: self.auth_token
        }

        try:
            with async_timeout.timeout(self.request_timeout):
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers, ssl=True) as response:
                        print(await response.text())
        except asyncio.TimeoutError as exception:
            # TODO better exception handling
            raise exception
    #
    # async def close(self) -> None:
    #     """Close open client session."""
    #     await self._session.close()
    #
    # async def __aenter__(self) -> "Huisbaasje":
    #     """Async enter."""
    #     print('entering context')
    #     return self
    #
    # async def __aexit__(self, *exc_info) -> None:
    #     """Async exit."""
    #     print('exiting context')
    #     await self.close()
