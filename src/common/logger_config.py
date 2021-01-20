import logging

# Set logging
logger_format = "[%(name)s][%(levelname)s] \
                %(message)s (%(filename)s:%(lineno)d)"
logging.basicConfig(format=logger_format, level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Logger is Configured.')
