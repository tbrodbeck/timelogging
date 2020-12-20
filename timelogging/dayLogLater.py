from . import getLog, startLogging, endLogging

"""shortcut import for time logging
logs day and time"""
log = getLog("%d %H:%M:%S", 30)
