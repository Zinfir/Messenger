"""Logger for client.py"""
import logging


LOGGER = logging.getLogger('client')
FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")
FILE_HANDLER = logging.FileHandler("logs/client.log", encoding='utf-8')
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(FILE_HANDLER)
LOGGER.setLevel(logging.DEBUG)


if __name__ == '__main__':
    CONSOLE = logging.StreamHandler()
    CONSOLE.setLevel(logging.DEBUG)
    CONSOLE.setFormatter(FORMATTER)
    LOGGER.addHandler(CONSOLE)
    LOGGER.info('Logging test')
