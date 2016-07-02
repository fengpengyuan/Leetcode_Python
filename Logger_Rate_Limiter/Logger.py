__author__ = 'fengpeng'


class Logger(object):
    def __init__(self):
        self.dict = {}

    def shouldPrintMessage(self, timestamp, message):
        if message in self.dict and timestamp - self.dict[message] < 10:
            return False
        dict[message] = timestamp
        return True