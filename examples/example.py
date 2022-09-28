import asyncio

from huisbaasje.huisbaasje import Huisbaasje


async def main(username: str, password: str):
    # Create a new client by supplying username and password
    huisbaasje = Huisbaasje(username, password)

    # Authenticate the client by attempting to login
    # On success, the user id and authentication are set on the client
    await huisbaasje.authenticate()
    print("Auth token: %s" % huisbaasje._auth_token)

    # In order to fetch the current energy consumption,
    # we first need to know the id of the customer and
    # the sources we can request the current energy consumption of.
    # Both the customer id and sources are stored inside the client.
    await huisbaasje.customer_overview()
    print("Customer ID: %s" % huisbaasje._customer_id)
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

    # The API for some reason has a protection that you cannot re-use the existing session to fetch the actuals.
    # All other requests are successful, but the server returns the following error when fetching the actual values:
    # "The request was a legal request, but the server is refusing to respond to it."
    # In order to make this example work, we start with a new client.
    huisbaasje = Huisbaasje(username, password)

    # When authenticated (or when authentication is invalid),
    # current_measurements() will automatically try to reauthenticate.
    current_measurements = await huisbaasje.current_measurements()
    print("Current measurements after reauthentication: %s" % current_measurements)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main("email@example.com", "password"))
