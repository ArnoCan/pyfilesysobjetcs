"""Local globs + regexpr.
"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

#
#######################
#

import filesysobjects.apppaths
import filesysobjects.pathtools
import testdata.filesysobjects

from filesysobjects import W_RE

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'
tdata = filesysobjects.apppaths.normapppathx(tdata, tpf='posix')

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase330(self):
        arg = tdata + r'/b\\\\"""[^/\\\\]/c[.].*"""'
        resX = [
            tdata + '/b/c/c.smod',
            tdata + '/b/c/c.pod',
            tdata + '/b/c/c.py',
            tdata + '/b/c/c.pl',
            tdata + '/b/c/c.pm',
            tdata + '/b/c/c.sh',
        ]

        from filesysobjects import V3K
        # import os
        if os.path.exists(tdata + '/b/c/c.pyc'):  # not V3K:
            resX.append(tdata + '/b/c/c.pyc')


        res = filesysobjects.pathtools.expandpath(arg, wildcards=W_RE)

#         print('4TEST:')
#         for i in res:
#             print(i)

        res = [ filesysobjects.apppaths.normapppathx(x, tpf='posix') for x in res]
        resX = [ filesysobjects.apppaths.normapppathx(x, tpf='posix') for x in resX]

        self.assertEqual(sorted(res), sorted(resX))


#
#######################
#

if __name__ == '__main__':
    unittest.main()
