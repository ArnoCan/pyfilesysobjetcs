"""Examples from documents for 'normpathx()'.
"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

from filesysobjects.paths import normpathx

#
#######################
#


class UseCase(unittest.TestCase):

#     def testCase001(self):
#         arg = '"""d"""'
#         resX = r'\\localhost\C$'
#         
#         res = normpathx(arg, tpf='posix')
# 
#         self.assertEqual(res, resX)

    def testCase010(self):
        arg = '\\\\localhost\\C$'
        resX = r'\\localhost\C$'
        
        res = normpathx(arg, tpf='win')
        self.assertEqual(res, resX)
        
    def testCase020(self):
        arg = '\\\\127.0.0.1\\C$'
        resX = r'\\127.0.0.1\C$'
        
        res = normpathx(arg, tpf='win')

        self.assertEqual(res, resX)
        

if __name__ == '__main__':
    unittest.main()

