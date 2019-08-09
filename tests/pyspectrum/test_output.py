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

"""Tests output.ColoredOutput.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pyspectrum import color
from pyspectrum import output

def test_assignment():
    """Tests getters and setters of output.ColoredOutput.
    """

    co = output.ColoredOutput()
    co.fg_color = color.CYAN
    co.bg_color = color.BG_BLUE
    assert co.fg_color == color.ansi_format(color.CYAN)
    assert co.bg_color == color.ansi_format(color.BG_BLUE)

def test_constructor():
    """Tests output.ColoredOutput.__init__.
    """

    co = output.ColoredOutput(color.RED, color.BG_WHITE)
    assert co.fg_color == color.ansi_format(color.RED)
    assert co.bg_color == color.ansi_format(color.BG_WHITE)

    co = output.ColoredOutput(color.RED)
    assert co.fg_color == color.ansi_format(color.RED)
    assert co.bg_color == color.ansi_format(color.RESET)

    co = output.ColoredOutput()
    assert co.fg_color == color.ansi_format(color.RESET)
    assert co.bg_color == color.ansi_format(color.RESET)

def test_reset():
    """Tests output.ColoredOutput.reset.
    """

    co = output.ColoredOutput()
    co.fg_color = color.CYAN
    co.reset()
    assert co.fg_color == color.ansi_format(color.RESET)

def run_all():
    """Runs all tests located in this module.
    """
    test_assignment()
    test_constructor()
    test_reset()
    print('test_output.py: All tests passed!')
