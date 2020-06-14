import asyncio

from huisbaasje.huisbaasje import Huisbaasje


async def authenticate(username: str, password: str):
    huisbaasje = Huisbaasje()

    user_id = await huisbaasje.authenticate(username, password)
    print("User id: %s" % huisbaasje.user_id)
    print("Auth token: %s" % huisbaasje.auth_token)

    await huisbaasje.sources()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(authenticate("email@example.com", "password"))

