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

"""Prints the ANSI colors.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pyspectrum
color = pyspectrum.color
output = pyspectrum.output

def color_line(fg_color, bg_color, text):
    """Prints a line of a designated foreground and backgroud color.

    Args:
      fg_color: The aforementioned foreground color.
      bg_color: The aforementioned background color.
      text: The desired name of the colors being printed.
    """

    out = output.ColoredOutput(fg_color, color.RESET)
    out.print(text.ljust(10), end='')

    out.fg_color = color.RESET
    out.bg_color = bg_color
    out.print(' ' * 10, end=' ')

    out.fg_color = fg_color + ';1'
    out.bg_color = color.RESET
    out.print(('Bright ' + text).ljust(10))

if __name__ == '__main__':
    color_line(color.FG_BLACK, color.BG_BLACK, 'Black')
    color_line(color.FG_RED, color.BG_RED, 'Red')
    color_line(color.FG_GREEN, color.BG_GREEN, 'Green')
    color_line(color.FG_YELLOW, color.BG_YELLOW, 'Yellow')
    color_line(color.FG_BLUE, color.BG_BLUE, 'Blue')
    color_line(color.FG_MAGENTA, color.BG_MAGENTA, 'Magenta')
    color_line(color.FG_CYAN, color.BG_CYAN, 'Cyan')
    color_line(color.FG_WHITE, color.BG_WHITE, 'White')
