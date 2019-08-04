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

"""Tests pyspectrum.color.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import color

def test_ansi_format():
    """Tests pyspectrum.color.ansi_format.
    """
    assert color.ansi_format(color.RED) == '\x1b[31m'
    assert color.ansi_format(color.BG_RED) == '\x1b[41m'
    assert color.RESET == '0'
    assert color.ansi_format(color.RESET) == '\x1b[0m'
