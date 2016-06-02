"""Get the caller name.
"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__='af90cc0c-de54-4a32-becd-06f5ce5a3a75'

__docformat__ = "restructuredtext en"

import unittest
import os

#
# set search for the call of 'myscript.sh'
from filesysobjects.FileSysObjects import setUpperTreeSearchPath
setUpperTreeSearchPath(None,'UseCases')

import filesysobjects.PySourceInfo

#
#######################
#

class CallUnits(unittest.TestCase):
    name=os.path.curdir+__file__

    output=True
    output=False

    def testCase000(self):
        ret = filesysobjects.PySourceInfo.getSourceFuncName()
        retx = 'testCase000'
        assert retx == ret

    def testCase001(self):
        ret = filesysobjects.PySourceInfo.getSourceFuncName(1)
        retx = 'testCase001'
        assert retx == ret

    def testCase002(self):
        ret = filesysobjects.PySourceInfo.getSourceFuncName(2)
        retx = 'run'
        assert retx == ret

    def testCase003(self):
        ret = filesysobjects.PySourceInfo.getSourceFuncName(3)
        retx = '__call__'
        assert retx == ret

    def testCase004(self):
        ret = filesysobjects.PySourceInfo.getSourceFuncName(4)
        retx = '_wrapped_run'
        assert retx == ret

#
#######################
#

if __name__ == '__main__':
    unittest.main()

