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
from filesysobjects.paths import normpathx


tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'

#
#######################
#

class UseCase(unittest.TestCase):

    def testCase010(self):
        self.maxDiff = None

        arg = [
            tdata + os.path.sep + 'b' + os.path.sep + 'c' + os.path.sep,
            tdata + os.path.sep + 'b0' + os.path.sep + 'c' + os.path.sep,
            tdata + os.path.sep + 'b1' + os.path.sep + 'c' + os.path.sep,
        ]
        arg_cut = [
            tdata + os.path.sep
        ]

        retX = [
            'b0\c\__init__.py',
            'b0\c\d\__init__.py',
            'b\c\__init__.py',
            'b\c\d\__init__.py',
        ]
        retX = [normpathx(x) for x in retX]
        retX = sorted(retX)

        ret = findpattern(
            *arg,
            topcutlist=arg_cut,
            whitelist=['.*/__init__.py$', ]
            )
        ret = sorted(ret)

#         print('4TEST:')
#         for i in ret:
#             print("            '" + str(i) + "',")


#         print('4TEST:' + str(ret))
#         print('4TEST:' + str(retX))

        self.assertEqual(ret, retX)


#
#######################
#
if __name__ == '__main__':
    unittest.main()

