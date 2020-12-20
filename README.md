# Installation

Install `timelogging` in your shell with the [Python Package Installer](https://pip.pypa.io/en/stable/):

```sh
pip3 install timelogging
```

# Usage

## Logging functionalities
### Time Log

The `log` function is designed to be a drop-in replacement for `print`:

```python
from timelogging.timeLog import log

log('This is a log entry.')
```

And this outputs the current time before the printout:

```
16:20:00 INFO    This is a log entry.
```

### Day Log

You can also add the current day within the timestamp:

```python
from timelogging.dayLog import log

log('This is a log entry.')
```

And this outputs the current time with the day before the printout:

```
31 16:20:00 INFO    This is a log entry.
```

### Cutom Log

Additionally, you can also create a custom timestamp formatting of the `log` function according to the [Python time formatting directives](https://docs.python.org/3/library/time.html#time.strftime) and a custom start log level according to the [Python logging level values](https://docs.python.org/3/library/logging.html#levels):

```python
from timelogging import configLog, log
configLog(timeFmt='%Y-%m-%d %H:%M:%S', startLevel=20)
log('This is a log entry.')
```

And this outputs your custom timestamp before the printout:

```
2020-12-31 16:20:00 INFO    This is a log entry.
```

## Changing the log level
### Setting the log level globally
The functions above set the log level immediately to `logging.INFO`. When this is not wanted, you can also import `timeLogLater`, `dayLogLater` to keep the log level at `logging.WARN` at start or set the `startLevel` parameter of the configLog function as you want.

Then you can import the functions `startLogging` and `endLogging` to change the log level on the fly.
```python
from timelogging.timeLogLater import log, startLogging, endLogging

log('not seeable')
startLogging()
log('seeable')
endLogging()
log('not seeable')
```
This example logs this output only:
```
16:20:00 INFO    seeable
```

### Changing the log level to `INFO` for one log entry
This is possible with the function `logOnce`. It changes the log level to `INFO` just for this log entry and after that it switches back to `WARN` (the default level). Simply use it as you would use `log`.
```python
from timelogging.timeLogLater import log, logOnce
log('not seeable')
logOnce('seeable')
log('not seeable')
```
This example logs the output of `logOnce` only, because otherwise the log level is set to `WARN`. This helps avoiding unwanted `INFO` logs:
```
16:20:00 INFO    seeable
```