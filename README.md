# Installation

Install `timelogging` in your shell with the [Python Package Installer](https://pip.pypa.io/en/stable/):

```sh
pip3 install timelogging
```

# Usage

## Logging functionalities
### Time Log

The `log` function is designed to be a drop-in replacement for `print`:

```python3
from timelogging.timeLog import log

log('This is a log entry.')
```

And this outputs the current time before the printout:

```
16:20:00 INFO    This is a log entry.
```

### Day Log

You can also add the current day within the timestamp:

```python3
from timelogging.dayLog import log

log('This is a log entry.')
```

And this outputs the current time with the day before the printout:

```
31 16:20:00 INFO    This is a log entry.
```

### Cutom Log

Additionally, you can also create a custom formatting for the `log` function.

The `getLog` function also helps avoiding to log unnecessary import imformation of other libraries when the function is called at a later stage of a python script.

```python3
import timelogging
log = timelogging.getLog('%Y-%m-%d %H:%M:%S')

log('This is a log entry.')
```

And this outputs your custom timestamp before the printout:

```
2020-12-31 16:20:00 INFO    This is a log entry.
```

## Change log level
The functions above set the log level immediately to `logging.INFO`. When this is not wanted, you can also import `timeLogLater`, `dayLogLater` to keep the log level at `logging.WARN` at start or set the `startLevel` parameter of the getLog function as you want.

Then you can import the functions `startLogging` and `endLogging` to change the log level on the fly.
```
from timelogging.timeLogLater import log, startLogging, endLogging

log('not seeable')
startLogging()
log('seeable')
endLogging()
log('not seeable')
```
This example only logs this output:
```
16:20:00 INFO    seeable
```