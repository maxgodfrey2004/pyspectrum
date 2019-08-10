# Copyright 2019 Max Godfrey
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys

_FILE_DIR = os.path.dirname(__file__)
sys.path.append(_FILE_DIR)

import color # pylint: disable=wrong-import-position
import output # pylint: disable=wrong-import-position

_BLACK_OUTPUT = output.ColoredOutput(color.FG_BLACK)
_RED_OUTPUT = output.ColoredOutput(color.FG_RED)
_GREEN_OUTPUT = output.ColoredOutput(color.FG_GREEN)
_YELLOW_OUTPUT = output.ColoredOutput(color.FG_YELLOW)
_BLUE_OUTPUT = output.ColoredOutput(color.FG_BLUE)
_MAGENTA_OUTPUT = output.ColoredOutput(color.FG_MAGENTA)
_CYAN_OUTPUT = output.ColoredOutput(color.FG_CYAN)
_WHITE_OUTPUT = output.ColoredOutput(color.FG_WHITE)

def black(*args, end='\n', sep=' '):
    """Behaves like print, but writes black text to the console.

    Args:
      end: The char outputted after print has finished.
      sep: The char placed in between every argument passed to print.
      *args: Arguments to be printed
    """
    _BLACK_OUTPUT.print(*args, end=end, sep=sep)

def red(*args, end='\n', sep=' '):
    """Behaves like print, but writes red text to the console.

    Args:
      end: The char outputted after print has finished.
      sep: The char placed in between every argument passed to print.
      *args: Arguments to be printed
    """
    _RED_OUTPUT.print(*args, end=end, sep=sep)

def green(*args, end='\n', sep=' '):
    """Behaves like print, but writes green text to the console.

    Args:
      end: The char outputted after print has finished.
      sep: The char placed in between every argument passed to print.
      *args: Arguments to be printed
    """
    _GREEN_OUTPUT.print(*args, end=end, sep=sep)

def yellow(*args, end='\n', sep=' '):
    """Behaves like print, but writes yellow text to the console.

    Args:
      end: The char outputted after print has finished.
      sep: The char placed in between every argument passed to print.
      *args: Arguments to be printed
    """
    _YELLOW_OUTPUT.print(*args, end=end, sep=sep)

def blue(*args, end='\n', sep=' '):
    """Behaves like print, but writes blue text to the console.

    Args:
      end: The char outputted after print has finished.
      sep: The char placed in between every argument passed to print.
      *args: Arguments to be printed
    """
    _BLUE_OUTPUT.print(*args, end=end, sep=sep)

def magenta(*args, end='\n', sep=' '):
    """Behaves like print, but writes magenta text to the console.

    Args:
      end: The char outputted after print has finished.
      sep: The char placed in between every argument passed to print.
      *args: Arguments to be printed
    """
    _MAGENTA_OUTPUT.print(*args, end=end, sep=sep)

def cyan(*args, end='\n', sep=' '):
    """Behaves like print, but writes cyan text to the console.

    Args:
      end: The char outputted after print has finished.
      sep: The char placed in between every argument passed to print.
      *args: Arguments to be printed
    """
    _CYAN_OUTPUT.print(*args, end=end, sep=sep)

def white(*args, end='\n', sep=' '):
    """Behaves like print, but writes white text to the console.

    Args:
      end: The char outputted after print has finished.
      sep: The char placed in between every argument passed to print.
      *args: Arguments to be printed
    """
    _WHITE_OUTPUT.print(*args, end=end, sep=sep)
