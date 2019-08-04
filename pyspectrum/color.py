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

"""Contains ANSI color attributes.
"""

ESC_CODE = '\x1b'
RESET = '0'

BLACK = '30'
RED = '31'
GREEN = '32'
YELLOW = '33'
BLUE = '34'
MAGENTA = '35'
CYAN = '36'
WHITE = '37'

BRIGHT_BLACK = '30;1'
BRIGHT_RED = '31;1'
BRIGHT_GREEN = '32;1'
BRIGHT_YELLOW = '33;1'
BRIGHT_BLUE = '34;1'
BRIGHT_MAGENTA = '35;1'
BRIGHT_CYAN = '36;1'
BRIGHT_WHITE = '37;1'

BG_BLACK = '40'
BG_RED = '41'
BG_GREEN = '42'
BG_YELLOW = '43'
BG_BLUE = '44'
BG_MAGENTA = '45'
BG_CYAN = '46'
BG_WHITE = '47'

BG_BRIGHT_BLACK = '40;1'
BG_BRIGHT_RED = '41;1'
BG_BRIGHT_GREEN = '42;1'
BG_BRIGHT_YELLOW = '43;1'
BG_BRIGHT_BLUE = '44;1'
BG_BRIGHT_MAGENTA = '45;1'
BG_BRIGHT_CYAN = '46;1'
BG_BRIGHT_WHITE = '47;1'

ESC_FORMAT = '{}[{}m'.format

def ansi_format(color_string):
    """Formats an ansi escape sequence with a given color string.

    Args
      color_string: The aforementioned color string to be placed in the escape
                    sequence.
    """
    return ESC_FORMAT(ESC_CODE, color_string)
