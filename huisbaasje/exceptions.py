"""Exceptions for Huisbaasje"""


class HuisbaasjeException(Exception):
    """Base exception of the Huisbaasje client"""
    pass


class HuisbaasjeUnauthenticatedException(HuisbaasjeException):
    """An attempt is made to perform a request which requires authentication while the client is not authenticated."""
    pass


class HuisbaasjeConnectionException(HuisbaasjeException):
    """An error occured in the connection with the API."""
    pass
