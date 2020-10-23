# Installation

Install `timelogging` in you shell with the [Python Package Installer](https://pip.pypa.io/en/stable/):

```sh
pip3 install timelogging
```

# Usage

## Time Log

The `log` function is designed to be a drop-in replacement for `print`:

```python3
from timelogging import timeLog as log

log('This', 'is', 'a', 'test.')
```

And this outputs the current time before the printout:

```
16:20:00  This is a test.
```

## Day Log

You can also add the current day within the timestamp:

```python3
from timelogging import timeLog as log

log('This', 'is', 'a', 'test.')
```

And this outputs the current time before the printout:

```
31 16:20:00  This is a test.
```

## Cutom Log

Additionally, you can also create a custom formatting for the log function:

You can also add the current day within the timestamp:

```python3
from timelogging import getLog
log = getLog('%Y-%m-%d %H:%M:%S')

log('This', 'is', 'a', 'test.')
```

And this outputs the current time before the printout:

```
2020-10-23 20:28:32  This is a test.
```
