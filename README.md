# Installation

Install `timelogging` in you shell with the [Python Package Installer](https://pip.pypa.io/en/stable/):
```sh
pip3 install timelogging
```

# Usage

The `log` function is designed to be a drop-in replacement for `print`:

```python3
from timelogging import log

log('This', 'is', 'a', 'test.')
```

And this outputs the current time before the printout:

```
16:20:00 INFO     This is a test.
```
