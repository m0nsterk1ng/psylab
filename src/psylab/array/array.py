# -*- coding: utf-8 -*-

# Copyright (c) 2010 Christopher Brown
#
# This file is part of Psylab.
#
# Psylab is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Psylab is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
# Comments and/or additions are welcome. Send e-mail to: cbrown1@pitt.edu.
#

#import numpy as np
from itertools import product

def indices(arr):
    return product(*tuple(xrange(y) for y in arr.shape))

def to_columns(arr):
    dvs = list(arr[i] for i in indices(arr))
    return np.array(zip(*tuple(indices(arr))) + [dvs])

def from_columns(arr):
    sh = tuple(1+int(max(x)) for x in arr[:-1])
    dv = arr[-1]
    ans = np.ones(shape=sh)

    j = 0
    for i in product(*tuple(xrange(y) for y in sh)):
        ans[i] = dv[j]
        j += 1

    return ans
