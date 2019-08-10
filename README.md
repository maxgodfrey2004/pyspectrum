# pyspectrum [![Build Status](https://travis-ci.com/maxgodfrey2004/pyspectrum.svg?branch=master)](https://travis-ci.com/maxgodfrey2004/pyspectrum) [![Maintainability](https://api.codeclimate.com/v1/badges/5aba341fdedbdb348937/maintainability)](https://codeclimate.com/github/maxgodfrey2004/pyspectrum/maintainability)
Cross platform colored output in Python.

## Examples

Using pyspectrum is really simple. After [installing](#installation), try the following script:

```python
import pyspectrum
pyspectrum.cyan('Hello, World!')
```

The program should output some colored text.

You can change background colors too (have a look in `pyspectrum/color.py` for a full list of foreground and background colors):

```python
from pyspectrum import color
from pyspectrum import output

colored_output = output.ColoredOutput(color.FG_WHITE, color.BG_RED)
colored_output.print('White text on a blue background!')
```

In the above example, the `print` method behaves almost exactly to the inbuilt equivalent. A `printf` function has also been implemented (why not). Extending the above example:

```python
colored_output.printf('4 * 2 = %d\n', 8)
```

Note that `ColoredOutput.printf` behaves very similarly to the `printf` that can be found in `stdio.h` of the C Programming Language. If you want a line feed at the end of your format string, you have to include it yourself.

## Requirements

Pyspectrum requires Python 3. There are no other dependencies!

Your terminal/console must be capable of interpreting ANSI escape sequences. Linux distributions (and the Windows Subsystem for Linux) come with these capabilities by default. The Windows 10 command prompt does as well - but not by default. This is not a problem though as `pyspectrum/output.py` turns such features on programmatically for the duration of program runtime only.

## Installation

If you haven't read the [requirements](#requirements) section, I would recommend that you do so now.

### Installing from PyPI

This project has not yet been uploaded to the Python Package Index, so this feature is currently not available. I will be sure to post instructions here when it is!

### Installing the repository

1. Clone the repository

```bash
git clone https://github.com/maxgodfrey2004/pyspectrum
````

2. Navigate to the repo's root directory

3. (Optional) Install pyspectrum locally (use either of the following)

```bash
pip3 install -e .
```

```bash
python3 -m pip3 install -e .
```
