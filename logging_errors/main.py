# import logging
import logging
from logging.handlers import RotatingFileHandler

# create a custom logger
logger = logging.getLogger(__name__)

# create handlers
console_handler = logging.StreamHandler()
# file_handler = logging.FileHandler()
rotating_file_handler = RotatingFileHandler(
    "app.log", maxBytes=2000, backupCount=5)
