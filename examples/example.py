import asyncio

from huisbaasje.huisbaasje import Huisbaasje


async def main(username: str, password: str):
    # Create a new client by supplying username and password
    huisbaasje = Huisbaasje(username, password)

    # Authenticate the client by attempting to login
    # On success, the user id and authentication are set on the client
    await huisbaasje.authenticate()
    print("Auth token: %s" % huisbaasje._auth_token)

    # In order to fetch the current energy consumption, we first need to know which sources we can use
    # to request the current energy consumption from. Sources are stored inside the client.
    await huisbaasje.customer_overview()
    print("Sources: %s" % huisbaasje._sources)

    # Request all actual energy consumption rates of the sources which correspond to the configured
    # source_types, by default equal to DEFAULT_SOURCE_TYPES in const.py.
    actuals = await huisbaasje.actuals()
    print("Actuals: %s" % actuals)

    # current_measurements() is a utility method which combines all steps above and only returns
    # the current values for each source, omitting the historical values.
    current_measurements = await huisbaasje.current_measurements()
    print("Current measurements: %s" % current_measurements)

    # Manually logout the client.
    huisbaasje.invalidate_authentication()

    # When authenticated (or when authentication is invalid),
    # current_measurements() will automatically try to reauthenticate.
    current_measurements = await huisbaasje.current_measurements()
    print("Current measurements after reauthentication: %s" % current_measurements)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main("email@example.com", "password"))
