import logging

# basicConfig sets the root logger level. Default is WARNING (30), which hides
# DEBUG and INFO. In Jupyter, the kernel may already have handlers — force=True
# re-applies this config so DEBUG/INFO are not silently dropped.
logging.basicConfig(
    format="\n{asctime} {lineno}:{levelname}:{name}:{message}-{process}-{thread}:",
    level=logging.DEBUG,
    filename="my_log.log",
    filemode="w",
    encoding="utf-8",
    force=True,
    style="{",
    # helps to format the log messages
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Logging functions write to stderr and return None — do not wrap them in print().
logger.debug("this is a debug message")
logger.info("this is an info message")
logger.warning("this is a warning message")
logger.error("this is an error message")
logger.critical("this is a critical message")

# exception() logs at ERROR and includes the traceback — use inside except.
try:
    1 / 0
except ZeroDivisionError:
    logger.exception("this is an exception message")
