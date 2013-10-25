# -*- coding: utf-8 -*-

# Copyright (c) 2010-2013 Christopher Brown
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
# along with Psylab.  If not, see <http://www.gnu.org/licenses/>.
#
# Bug reports, bug fixes, suggestions, enhancements, or other 
# contributions are welcome. Go to http://code.google.com/p/psylab/ 
# for more information and to contribute. Or send an e-mail to: 
# cbrown1@pitt.edu.
#

'''
PsyLab - Psychophysics Lab

A loose collection of modules useful for various aspects of running
psychophysical experiments, although several might be more generally
useful.

In addition to the modules that are imported automatically, others include:

subject_manager: User interface with many features for a subject info database
tdt2: interface tucker davis system II hardware via the serial port

'''

__version__ = '0.3.1'

#from array import array, nanproduct, nanmean
#from dataview import dataview
#from misc import csv_inspect, plot_tools, path_tools
from . import misc
from . import signal
from . import stats
from . import gustav
#import stats
#import gustav

