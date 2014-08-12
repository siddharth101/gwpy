#!/usr/bin/env python

# Copyright (C) Duncan Macleod (2014)
#
# This file is part of GWpy.
#
# GWpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GWpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GWpy.  If not, see <http://www.gnu.org/licenses/>.

"""GWpy Example: plotting the rate versus time of a table of event triggers

Problem
-------

I would like to study the rate at which event triggers are generated by the
`ExcessPower` gravitational-wave burst detection algorithm, over a small
stretch of data.

The data from which these events were generated are a simulation of Gaussian noise
with the Advanced LIGO design spectrum, and so don't actually contain any real
gravitational waves, but will help tune the algorithm to improve detection of
future, real signals.
"""

from gwpy import version
__author__ = "Duncan Macleod <duncan.macleod@ligo.org>"
__version__ = version.version

from gwpy.table.lsctables import SnglBurstTable

# read triggers
events = SnglBurstTable.read('../gwpy/tests/data/'
                             'H1-LDAS_STRAIN-968654552-10.xml.gz')

# calculate the event rate
rate = events.event_rate(1, start=968654552, end=968654562)

# make a plot
plot = rate.plot()
plot.set_xlim(968654552, 968654562)
plot.set_ylabel('Event rate [Hz]')
plot.set_title('LIGO Hanford Observatory event rate for GW100916')

if __name__ == '__main__':
    try:
        outfile = __file__.replace('.py', '.png')
    except NameError:
        pass
    else:
        plot.save(outfile)
        print("Example output saved as\n%s" % outfile)
