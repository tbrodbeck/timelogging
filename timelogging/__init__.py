import logging
class Logger:
    def __init__(self, timeFmt: str, startLevel: int):
        logging.basicConfig(
            format="%(asctime)s %(levelname)-7s %(message)s",
            level=startLevel,
            datefmt=timeFmt,
        )
def log(*args):
    """Logs the arguments given"""
    infoTxt = str(args[0]) if len(args) else ""
    for arg in args[1:]:
        infoTxt += " " + str(arg)
    logging.info(infoTxt)

def logOnce(*args):
    """Logs the arguments given. Before logging the log level is set to `INFO` and after logging the log level is set to `WARN`"""
    startLogging()
    log(*args)
    endLogging()

def configLog(timeFmt="%H:%M:%S", startLevel=logging.INFO):
    """Creates a log function with a custom time format and a custom start log level.
    Args:
        timeFmt (str, optional): Time formatting according to the official Python time formatting directives. Defaults to "%H:%M:%S".
        startLevel ([type], optional): Log level according to the Python logging level values. Defaults to logging.INFO."""
    Logger(timeFmt, startLevel)

def startLogging():
    """sets the log level to `INFO`"""
    logging.getLogger().setLevel(logging.INFO)

def endLogging():
    """sets the log level to `WARN` (the default level) """
    logging.getLogger().setLevel(logging.WARN)
