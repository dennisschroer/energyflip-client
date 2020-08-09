"""Huisbaasje constants"""

API_HOST = "mijnaurum.nl"

AUTHENTICATION_PATH = "/user/v2/authentication"
"""Path to perform authentication. Result is a user id and an auth token"""

SOURCE_TYPE_ELECTRICITY = "electicity"
SOURCE_TYPE_ELECTRICITY_IN = "electricityIn"
SOURCE_TYPE_ELECTRICITY_IN_LOW = "electricityInLow"
SOURCE_TYPE_ELECTRICITY_OUT = "electricityOut"
SOURCE_TYPE_ELECTRICITY_OUT_LOW = "electricityOutLow"
SOURCE_TYPE_ELECTRICITY_EXPECTED = "electricityExpected"
SOURCE_TYPE_ELECTRICITY_GOAL = "electricityGoal"
SOURCE_TYPE_GAS = "gas"
SOURCE_TYPE_GAS_EXPECTEC = "gasExpected"
SOURCE_TYPE_GAS_GOAL = "gasGoal"

DEFAULT_SOURCE_TYPES = [SOURCE_TYPE_ELECTRICITY,
                        SOURCE_TYPE_ELECTRICITY_IN,
                        SOURCE_TYPE_ELECTRICITY_IN_LOW,
                        SOURCE_TYPE_ELECTRICITY_OUT,
                        SOURCE_TYPE_ELECTRICITY_OUT_LOW,
                        SOURCE_TYPE_ELECTRICITY_EXPECTED,
                        SOURCE_TYPE_ELECTRICITY_GOAL,
                        SOURCE_TYPE_GAS,
                        SOURCE_TYPE_GAS_EXPECTEC,
                        SOURCE_TYPE_GAS_GOAL]
"""Default source types to fetch if none are specified."""

SOURCES_PATH = "/user/v2/users/%s/sources"
"""Path to request sources. Should be formatted with user id."""

ACTUALS_PATH = "/user/v2/users/%s/actuals"
"""Path to request actual values. Should be formatted with user id."""

AUTH_TOKEN_HEADER = "Auth-Token"
"""Header which contains (in response) or should contain (in request) the authentication token"""
