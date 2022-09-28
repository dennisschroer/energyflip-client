"""Exceptions for EnergyFlip"""


class EnergyFlipException(Exception):
    """Base exception of the EnergyFlip client"""
    pass


class EnergyFlipUnauthenticatedException(EnergyFlipException):
    """An attempt is made to perform a request which requires authentication while the client is not authenticated."""
    pass


class EnergyFlipConnectionException(EnergyFlipException):
    """An error occured in the connection with the API."""
    pass
