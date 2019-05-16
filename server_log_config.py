"""Logger for server.py"""
import logging
from logging.handlers import TimedRotatingFileHandler

LOGGER = logging.getLogger('server')
FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")

DAILY_ROTATING_HANDLER = TimedRotatingFileHandler(
    "log/server.log",
    when="D",
    interval=1,
    backupCount=1,
    encoding='utf-8'
)
DAILY_ROTATING_HANDLER.setLevel(logging.DEBUG)
DAILY_ROTATING_HANDLER.setFormatter(FORMATTER)

LOGGER.addHandler(DAILY_ROTATING_HANDLER)
LOGGER.setLevel(logging.DEBUG)


if __name__ == '__main__':
    CONSOLE = logging.StreamHandler()
    CONSOLE.setLevel(logging.DEBUG)
    CONSOLE.setFormatter(FORMATTER)
    LOGGER.addHandler(CONSOLE)
    LOGGER.info('Logging test')
