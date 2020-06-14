import asyncio
import aiohttp
import async_timeout
from yarl import URL

from .const import API_HOST, AUTHENTICATION_PATH


class Huisbaasje:
    """Client to connect with Huisbaasje"""

    def __init__(self, request_timeout: int = 10):
        self.request_timeout = request_timeout

    async def authenticate(self, username: str, password: str):
        """Log in using username and password. Returns the user id."""
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
                        return json['userId']

        except asyncio.TimeoutError as exception:
            # TODO better exception handling
            raise exception
        except (aiohttp.ClientError) as exception:
            # TODO better exception handling
            raise exception
