# Installation

Install `timelogging` in your shell with the [Python Package Installer](https://pip.pypa.io/en/stable/):

```sh
pip3 install timelogging
```

# Usage

## Time Log

The `log` function is designed to be a drop-in replacement for `print`:

```python3
from timelogging.timeLog import log

log('This is a log entry.')
```

And this outputs the current time before the printout:

```
16:20:00  This is a log entry.
```

## Day Log

You can also add the current day within the timestamp:

```python3
from timelogging.dayLog import log

log('This is a log entry.')
```

And this outputs the current time with the day before the printout:

```
31 16:20:00  This is a log entry.
```

## Cutom Log

Additionally, you can also create a custom formatting for the `log` function.

The `getLog` function also helps avoiding to log unnecessary import imformation of other libraries when the function is called at a later stage of a python script.

```python3
from timelogging
log = timelogging.getLog('%Y-%m-%d %H:%M:%S')

log('This is a log entry.')
```

And this outputs your custom timestamp before the printout:

```
2020-12-31 16:20:00  This is a log entry.
```
