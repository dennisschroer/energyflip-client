from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop, TestServer
from aiohttp.web_request import Request

from huisbaasje import Huisbaasje
from huisbaasje.const import AUTH_TOKEN_HEADER


class HuisbaasjeTestCase(AioHTTPTestCase):
    async def get_application(self):
        async def authenticate(request: Request):
            json = await request.json()
            assert json["loginName"] == "username"
            assert json["password"] == "password"
            with open("responses/authentication.json") as file:
                return web.Response(
                    content_type="application/json",
                    headers={AUTH_TOKEN_HEADER: "token"},
                    text=file.read()
                )

        async def sources(request: Request):
            assert request.headers[AUTH_TOKEN_HEADER] == "token"
            with open("responses/sources.json") as file:
                return web.Response(
                    content_type="application/json",
                    text=file.read()
                )

        async def actuals(request: Request):
            assert request.headers[AUTH_TOKEN_HEADER] == "token"
            assert request.query["sources"] == "sourceId5,sourceId1,sourceId2,sourceId3,sourceId4," \
                                               "sourceId6,sourceId7,sourceId8,sourceId9,sourceId10"
            with open("responses/actuals.json") as file:
                return web.Response(
                    content_type="application/json",
                    text=file.read()
                )

        app = web.Application()
        app.router.add_post('/user/v2/authentication', authenticate)
        app.router.add_get('/user/v2/users/1234/sources', sources)
        app.router.add_get('/user/v2/users/1234/actuals', actuals)
        return app

    @unittest_run_loop
    async def test_authenticate_success(self):
        huisbaasje = Huisbaasje("username", "password", api_scheme="http", api_host="localhost",
                                api_port=self.server.port)
        await huisbaasje.authenticate()

        assert huisbaasje.is_authenticated()
        assert huisbaasje.get_user_id() == "1234"
        assert huisbaasje._auth_token == "token"

    @unittest_run_loop
    async def test_sources(self):
        huisbaasje = Huisbaasje("username", "password", api_scheme="http", api_host="localhost",
                                api_port=self.server.port)
        await huisbaasje.authenticate()
        await huisbaasje.sources()

        assert huisbaasje.get_source_ids() == [
            "sourceId5",
            "sourceId1",
            "sourceId2",
            "sourceId3",
            "sourceId4",
            "sourceId6",
            "sourceId7",
            "sourceId8",
            "sourceId9",
            "sourceId10"
        ]

    @unittest_run_loop
    async def test_actuals(self):
        huisbaasje = Huisbaasje("username", "password", api_scheme="http", api_host="localhost",
                                api_port=self.server.port)
        await huisbaasje.authenticate()
        await huisbaasje.sources()
        actuals = await huisbaasje.actuals()

        assert len(actuals) == 10
        assert "electricity" in actuals
        assert "electricityIn" in actuals
        assert "electricityInLow" in actuals
        assert "electricityOut" in actuals
        assert "electricityOutLow" in actuals
        assert "electricityExpected" in actuals
        assert "electricityGoal" in actuals
        assert "gas" in actuals
        assert "gasExpected" in actuals
        assert "gasGoal" in actuals
        assert actuals["electricity"]["type"] == "electricity"
        assert actuals["electricity"]["source"] == "sourceId5"
        assert len(actuals["electricity"]["measurements"]) == 29
        assert actuals["electricity"]["thisDay"]["value"] == 1.7883327720000002
        assert actuals["electricity"]["thisWeek"]["value"] == 3.931665413

    @unittest_run_loop
    async def test_current_measurements(self):
        huisbaasje = Huisbaasje("username", "password", api_scheme="http", api_host="localhost",
                                api_port=self.server.port)
        current_measurements = await huisbaasje.current_measurements()

        assert len(current_measurements) == 10
        assert "electricity" in current_measurements
        assert "electricityIn" in current_measurements
        assert "electricityInLow" in current_measurements
        assert "electricityOut" in current_measurements
        assert "electricityOutLow" in current_measurements
        assert "electricityExpected" in current_measurements
        assert "electricityGoal" in current_measurements
        assert "gas" in current_measurements
        assert "gasExpected" in current_measurements
        assert "gasGoal" in current_measurements
        assert current_measurements["electricity"]["measurement"]["rate"] == 246.66666666666669
        assert current_measurements["electricity"]["measurement"]["time"] == "2020-06-14T11:08:20.000Z"
        assert current_measurements["electricity"]["thisDay"]["value"] == 1.7883327720000002
        assert current_measurements["electricity"]["thisDay"]["cost"] == 0.35766655440000006
        assert current_measurements["electricity"]["thisWeek"]["value"] == 3.931665413
        assert current_measurements["electricity"]["thisWeek"]["cost"] == 0.7863330826000001
