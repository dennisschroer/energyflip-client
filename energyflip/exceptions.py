"""Exceptions for Energyflip"""


class EnergyflipException(Exception):
    """Base exception of the Energyflip client"""
    pass


class EnergyflipUnauthenticatedException(EnergyflipException):
    """An attempt is made to perform a request which requires authentication while the client is not authenticated."""
    pass


class EnergyflipConnectionException(EnergyflipException):
    """An error occured in the connection with the API."""
    pass
