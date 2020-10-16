from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop, TestServer
from aiohttp.web_request import Request

from huisbaasje import Huisbaasje
from huisbaasje.const import AUTH_TOKEN_HEADER


class HuisbaasjeTestCase(AioHTTPTestCase):
    async def get_application(self):
        async def authenticate(request: Request):
            assert request.body_exists
            json = await request.json()
            assert json["loginName"] == "username"
            assert json["password"] == "password"
            return web.Response(
                headers={
                    "Content-Type": "application/json",
                    AUTH_TOKEN_HEADER: "token"
                },
                text="{\"userId\":\"1234\"}"
            )

        app = web.Application()
        app.router.add_post('/user/v2/authentication', authenticate)
        return app

    @unittest_run_loop
    async def test_authenticate_success(self):
        huisbaasje = Huisbaasje("username", "password", api_scheme="http", api_host="localhost",
                                api_port=self.server.port)
        await huisbaasje.authenticate()

        assert huisbaasje.is_authenticated()
        assert huisbaasje.get_user_id() == "1234"
        assert huisbaasje._auth_token == "token"
