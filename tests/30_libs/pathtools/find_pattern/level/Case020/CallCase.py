"""Check default values, and with defaults as passed parameters.
"""
from __future__ import absolute_import
from __future__ import print_function

_author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.4'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

import filesysobjects.apppaths
import testdata.filesysobjects

from filesysobjects.pathtools import findpattern
from filesysobjects import RTE, RTE_WIN32

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'

#
#######################
#

class UseCase(unittest.TestCase):

    def testCase010(self):
        arg = tdata

        #ret = findpattern(arg, spf='posix', tpf='local')
        ret = findpattern(
            arg,
            topcutlist=[arg+os.sep],
            whitelist=['.*[.]py'],
            blacklist=['.*/__init__[.]py', '.*__pycache__.*', '.*[.]pyc'],
            level=1
            )

        if RTE & RTE_WIN32:
            retX = ['b\\b.py', 'b1\\b1.py', 'b2\\b2.py', '..py', 'b0\\b0.py']

        else:
            retX = ['b/b.py', 'b1/b1.py', 'b2/b2.py', '..py', 'b0/b0.py']

        self.assertEqual(sorted(ret), sorted(retX))


#
#######################
#
if __name__ == '__main__':
    unittest.main()

