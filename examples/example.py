import asyncio

from huisbaasje.huisbaasje import Huisbaasje


async def authenticate(username: str, password: str):
    huisbaasje = Huisbaasje()

    await huisbaasje.authenticate(username, password)
    print("User id: %s" % huisbaasje._user_id)
    print("Auth token: %s" % huisbaasje._auth_token)

    await huisbaasje.sources()

    print("Sources: %s" % huisbaasje._sources)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(authenticate("email@example.com", "password"))

