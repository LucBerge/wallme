# coding: utf8

class bcolors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    CR = '\033[F'


class Log(object):
    def __init__(self, name):
        self.name = name

    def debug(self, msg, CR=False, flush=False):
        if (CR is True):
            print(bcolors.CR + msg, flush=flush)
        else:
            print(msg, flush=flush)

    def warning(self, msg, flush=False):
        print(bcolors.WARNING + "WARNING: " + bcolors.END + msg, flush=flush)

    def error(self, msg, flush=False):
        print(bcolors.FAIL + "ERROR: " + bcolors.END + msg, flush=flush)


logger = Log("wallme")
