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

"""Coloured output utilities.

This file uses a few abbreviations, the most common of which are `fg` meaning
`foreground`, and `bg` meaning `background`.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import ctypes
import os

import color

def enable_windows_ansi():
    """Enables ansi escape sequences on the Windows command prompt.

    Note that the setting will be returned to its default when the program
    finishes running.
    """
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# Enable ansi codes on the terminal if we are using Windows ('nt'). Note that
# this only enables them while the code is running.
if os.name == 'nt':
    enable_windows_ansi()

ANSI_RESET = color.ansi_format(color.RESET)

class ColoredOutput(object):
    """Outputs colored text to the terminal.
    """

    def __init__(self, fg_color=color.RESET, bg_color=color.RESET):
        self._fg_color = fg_color
        self._bg_color = bg_color

    def print(self, *args, end='\n', sep=' '):
        """Behaves like print, but outputs colors before and after print args.

        Args:
          *args: Arguments passed to print.
          end: The char outputted after print has printed its arguments. Passed
               to print.
          sep: The char placed in between each argument given to print. Passed
               to print.
        """
        ansi_output = ''
        if self.fg_color != ANSI_RESET:
            ansi_output += self.fg_color
        if self.bg_color != ANSI_RESET:
            ansi_output += self.bg_color

        print(ansi_output, end='')
        print(*args, end='', sep=sep)
        print(color.ansi_format(color.RESET), end=end)

    def printf(self, string, *tokens):
        """Prints a colorful formatted string.

        The colors of the outputted string correspond to self._fg_color and
        self._bg_color.

        Args:
          string: The string (including format tokens) to be printed
          *tokens: The values which the tokens in the original string will be
                   substituted for.
        """
        try:
            formatted = string % tokens
        except TypeError as err:
            raise err

        ansi_output = ''
        if self.fg_color != ANSI_RESET:
            ansi_output += self.fg_color
        if self.bg_color != ANSI_RESET:
            ansi_output += self.bg_color

        print(ansi_output, end='')
        print(formatted, end='')
        print(ANSI_RESET, end='')

    def reset(self):
        """Resets the foreground and background colors to their defaults.
        """
        self._set_fg_color(color.RESET)
        self._set_bg_color(color.RESET)

    @property
    def fg_color(self):
        """Returns the formatted foreground color.
        """
        return color.ansi_format(self._fg_color)

    @fg_color.setter
    def fg_color(self, new_color):
        """Changes the foreground color.

        Args:
          new_color: The new color which the foreground is being set to.
        """
        self._set_fg_color(new_color)

    @property
    def bg_color(self):
        """Returns the formatted background color.
        """
        return color.ansi_format(self._bg_color)

    @bg_color.setter
    def bg_color(self, new_color):
        """"Changes the background color.

        Args:
          new_color: The new color which the background is being set to.
        """
        self._set_bg_color(new_color)

    def _set_fg_color(self, new_color):
        """Internally changes the foreground color.
        """
        self._fg_color = new_color

    def _set_bg_color(self, new_color):
        """Internally changes the background color.
        """
        self._bg_color = new_color
