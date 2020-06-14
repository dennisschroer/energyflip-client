"""Huisbaasje constants"""

API_HOST = "mijnaurum.nl"

AUTHENTICATION_PATH = "/user/v2/authentication"
"""Path to perform authentication. Result is a user id and an auth token"""

SOURCES_PATH = "/user/v2/users/%s/sources"
"""Path to request sources. Should be formatted with user id."""

AUTH_TOKEN_HEADER = "Auth-Token"
"""Header which contains (in response) or should contain (in request) the authentication token"""

SOURCE_TYPES = {
    "electricityIn": "electricityIn",
    "electricityInLow": "electricityInLow",
    "electricityOut": "electricityOut",
    "electricityOutLow": "electricityOutLow",
    "electricity": "electricity",
    "electricityExpected": "electricityExpected",
    "electricityGoal": "electricityGoal",
    "gas": "gas",
    "gasExpected": "gasExpected",
    "gasGoal": "gasGoal"
}
