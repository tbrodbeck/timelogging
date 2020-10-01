import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)  # make sure to execute this before importing the WML client. Otherwise it wont work


def log(*args):
    """logs the arguments given
    this function enables a timestamp for every execution; this is a replacement for `print`"""
    infoTxt = str(args[0]) if len(args) else ""
    for arg in args[1:]:
        infoTxt += " " + str(arg)
    logging.info(infoTxt)
