"""Utility decorators"""
import inspect
import logging
from functools import wraps


LOGGER = logging.getLogger('client')


def caller():
    """Return caller function name"""
    return inspect.stack()[2][3]


def log(logger_name):
    """
    Decorator, log debug info about function.
    Save function name, args, kwargs, caller function name.
    """
    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            logger = logging.getLogger(logger_name)
            logger.debug(
                'Function %s run with args %s and kwargs %s, called from %s function',
                func.__name__,
                args,
                kwargs,
                caller()
            )
            res = func(*args, **kwargs)
            return res
        return decorated
    return decorator
