import sys
import logging

formatter = logging.Formatter('%(name)s:%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('%s.log' % __name__)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")
logger.exception("Exception")

# Ref - https://docs.python.org/3/library/logging.html
#     - https://www.youtube.com/watch?v=jxmzY9soFXg
######################################################

# Custom 

class Logger(object):

    def __init__(self, logger_name=None):
        self.logger = logging.getLogger(logger_name if logger_name else self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.propagate = False
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def exception(self, msg, *args, exc_info=True, **kwargs):
        self.logger.exception(msg, *args, exc_info=exc_info, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)


class ColorLogger:

    WARNING = '\033[93m'
    FAIL = '\033[91m'
    DEBUG = '\033[92m'
    FATAL = '\033[31m'
    NORMAL = '\033[37m'

    def __init__(self, filename):
        self.file = filename

    def debug(self, message):
        print(f"{self.DEBUG}Debug ==> {self.file} => [{datetime.now()}]: {message} {self.NORMAL}")

    def error(self, message):
        print(f"{self.FAIL}Serious ==> {self.file} => [{datetime.now()}]: {message}{self.NORMAL}")

    def warn(self, message):
        print(f"{self.WARNING}Warning ==> {self.file} => [{datetime.now()}]: {message}{self.NORMAL}")

    def fatal(self, message):
        print(f"{self.FATAL}DEFCON 1 ==> {self.file} => [{datetime.now()}]: {message}{self.NORMAL}")

    @staticmethod
    def normal(message):
        print(message)
