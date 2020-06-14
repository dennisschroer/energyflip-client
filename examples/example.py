import asyncio

from huisbaasje.huisbaasje import Huisbaasje


async def main(username: str, password: str):
    huisbaasje = Huisbaasje(username, password)

    await huisbaasje.authenticate()
    print("User id: %s" % huisbaasje._user_id)
    print("Auth token: %s" % huisbaasje._auth_token)

    await huisbaasje.sources()
    print("Sources: %s" % huisbaasje._sources)

    actuals = await huisbaasje.actuals()
    print("Actuals: %s" % actuals)

    current_measurements = await huisbaasje.current_measurements()
    print("Current measurements: %s" % current_measurements)

    huisbaasje.invalidate_authentication()
    current_measurements = await huisbaasje.current_measurements()
    print("Current measurements after reauthentication: %s" % current_measurements)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main("email@example.com", "password"))
