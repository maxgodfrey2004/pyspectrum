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

"""Runs all testing files located in the directory.

There are far nicer ways which this can be done, including `pytest`, `nose`,
`tox` and other similar packages, however I have struggled in making each of
these work. At this stage, it is faster for me to test my code manually.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import test_color
import test_output

test_color.run_all()
test_output.run_all()
