import logging


class Logger:
    def __init__(self, datefmt: str, startLevel: int):
        """datefmt: string representation of the timestamp"""

        self.logging = logging
        logging.basicConfig(
            format="%(asctime)s %(levelname)-7s %(message)s",
            level=startLevel,
            datefmt=datefmt,
        )

    def log(self, *args):
        """logs the arguments given
        this function enables a timestamp for every execution; this is a replacement for `print`"""
        infoTxt = str(args[0]) if len(args) else ""
        for arg in args[1:]:
            infoTxt += " " + str(arg)
        self.logging.info(infoTxt)

    def logOnce(self, *args):
        startLogging()
        self.log(*args)
        endLogging()

def getLog(datefmt="%H:%M:%S", startLevel=logging.INFO):
    """create a log function quickly without having to use the constructor
    datefmt: string representation of the timestamp"""
    logger = Logger(datefmt, startLevel)
    return logger.log, logger.logOnce

def startLogging():
    logging.getLogger().setLevel(logging.INFO)

def endLogging():
    logging.getLogger().setLevel(logging.WARN)
