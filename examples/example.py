import asyncio

from huisbaasje.huisbaasje import Huisbaasje


async def authenticate(username: str, password: str):
    huisbaasje = Huisbaasje()
    user_id = await huisbaasje.authenticate(username, password)
    print(user_id)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(authenticate("email@example.com", "password"))

