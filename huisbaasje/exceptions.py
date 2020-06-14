"""Exceptions for Huisbaasje"""


class HuisbaasjeException(Exception):
    pass


class HuisbaasjeAuthenticationException(HuisbaasjeException):
    pass


class HuisbaasjeConnectionException(HuisbaasjeException):
    pass
