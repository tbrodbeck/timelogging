import logging


class Logger:
    def __init__(self, datefmt="%H:%M:%S"):
        """datefmt: string representation of the timestamp"""

        self.logging = logging
        logging.basicConfig(
            format="%(asctime)s  %(message)s",
            level=logging.INFO,
            datefmt=datefmt,
        )

    def log(self, *args):
        """logs the arguments given
        this function enables a timestamp for every execution; this is a replacement for `print`"""
        infoTxt = str(args[0]) if len(args) else ""
        for arg in args[1:]:
            infoTxt += " " + str(arg)
        self.logging.info(infoTxt)


def getLog(datefmt="%H:%M:%S"):
    """create a log function quickly without having to use the constructor
    datefmt: string representation of the timestamp"""
    logger = Logger(datefmt)
    return logger.log
