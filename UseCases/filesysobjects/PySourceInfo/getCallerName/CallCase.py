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

def _funcDummyLvl0(sx=2):
    return (filesysobjects.PySourceInfo.getCallerName(sx), None, )

def _funcDummyLvl1(sx=1):
    return (filesysobjects.PySourceInfo.getCallerName(sx), _funcDummyLvl0(sx+1), )

def _funcDummyLvl2(sx=1):
    return (filesysobjects.PySourceInfo.getCallerName(sx), _funcDummyLvl1(sx+1), )

def _funcDummyLvl3(sx=1):
    return (filesysobjects.PySourceInfo.getCallerName(sx), _funcDummyLvl2(sx+1), )


class CallUnits(unittest.TestCase):
    name=os.path.curdir+__file__

    output=True
    output=False

    def testCase000(self):
        ret = _funcDummyLvl0()
        retx = ('UseCases.filesysobjects.PySourceInfo.getCallerName.CallCase', None,)
        assert retx == ret

    def testCase001(self):
        ret = _funcDummyLvl1()
        retx = ('UseCases.filesysobjects.PySourceInfo.getCallerName.CallCase', ('UseCases.filesysobjects.PySourceInfo.getCallerName.CallCase', None))
        assert retx == ret

    def testCase002(self):
        ret = _funcDummyLvl2()
        retx = ('UseCases.filesysobjects.PySourceInfo.getCallerName.CallCase', ('UseCases.filesysobjects.PySourceInfo.getCallerName.CallCase', ('UseCases.filesysobjects.PySourceInfo.getCallerName.CallCase', None)))
        assert retx == ret

    def testCase003(self):
        ret = _funcDummyLvl3()
        retx = ('UseCases.filesysobjects.PySourceInfo.getCallerName.CallCase', ('UseCases.filesysobjects.PySourceInfo.getCallerName.CallCase', ('UseCases.filesysobjects.PySourceInfo.getCallerName.CallCase', ('UseCases.filesysobjects.PySourceInfo.getCallerName.CallCase', None))))
        assert retx == ret

#
#######################
#

if __name__ == '__main__':
    unittest.main()

