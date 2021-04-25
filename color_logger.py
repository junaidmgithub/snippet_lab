from datetime import datetime


class Log:

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
