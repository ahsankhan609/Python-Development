# import logging
import logging
from logging.handlers import RotatingFileHandler

# create a custom logger
logger = logging.getLogger(__name__)

# create handlers
console_handler = logging.StreamHandler()
# file_handler = logging.FileHandler()
rotating_file_handler = RotatingFileHandler(
    "logging_errors/app.log", maxBytes=2000, backupCount=5)

# set level of logging
console_handler.setLevel(logging.WARNING)
rotating_file_handler.setLevel(logging.ERROR)

# creating formatters and add them to handlers
logging_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add handlers to the logger
console_handler.setFormatter(logging_format)
rotating_file_handler.setFormatter(logging_format)

logger.addHandler(console_handler)
logger.addHandler(rotating_file_handler)

# log Messages
logger.warning("This is a warning")
logger.error("This is an error")

