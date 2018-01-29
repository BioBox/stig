# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details
# http://www.gnu.org/licenses/gpl-3.0.txt

from ._number import (NumberFloat, NumberInt, pretty_float, DataCountConverter)
from ._string import (striplines, strwidth, strcrop, stralign, crop_and_align)

from types import SimpleNamespace
convert = SimpleNamespace(bandwidth=DataCountConverter(),
                          size=DataCountConverter())
