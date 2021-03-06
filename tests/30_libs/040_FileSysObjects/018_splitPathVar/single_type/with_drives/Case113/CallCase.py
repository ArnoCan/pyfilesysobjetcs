from __future__ import absolute_import
from linecache import getline


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__='af90cc0c-de54-4a32-becd-06f5ce5a3a75'

__docformat__ = "restructuredtext en"

import unittest
import os,sys

import filesysobjects.FileSysObjects
import pysourceinfo.PySourceInfo

#
#######################
#


class CallUnits(unittest.TestCase):
    """Network resources IEEE.1003.1/CIFS/SMB/UNC - respect hostname
    """

    def testCase000(self):
        
        start = filesysobjects.FileSysObjects.normpathX('//hostname/tests//////a/b/hostname//c////////d/tests/b///c')
        startRef = [('SHARE', 'hostname', 'tests', filesysobjects.FileSysObjects.normpathX('a/b/hostname/c/d/tests/b/c'))]
        ret = filesysobjects.FileSysObjects.splitPathVar(start,appsplit=True)
        self.assertEqual(startRef, ret) 


        top = filesysobjects.FileSysObjects.normpathX('/hostname')
        topRef = [('LFSYS', '', '', filesysobjects.FileSysObjects.normpathX('/hostname'))]
        ret = filesysobjects.FileSysObjects.splitPathVar(top,appsplit=True)
        self.assertEqual(topRef, ret) 


        top0ref=filesysobjects.FileSysObjects.normpathX('//hostname/tests/a/b/hostname')
        topRef = [('SHARE', 'hostname', 'tests', filesysobjects.FileSysObjects.normpathX('a/b/hostname'))]
        top = filesysobjects.FileSysObjects.getTopFromPathString(top, [start], **{'ias':True})
        ret = filesysobjects.FileSysObjects.splitPathVar(top,appsplit=True)

        self.assertEqual(top0ref, top) 
        self.assertEqual(topRef, ret) 
        pass

    def testCase020(self):
        
        start = filesysobjects.FileSysObjects.normpathX('//hostname/tests//////a/b/hostname//c////////d/tests/b///c')
        startRef = [('SHARE', 'hostname', 'tests', filesysobjects.FileSysObjects.normpathX('a/b/hostname/c/d/tests/b/c'))]
        ret = filesysobjects.FileSysObjects.splitPathVar(start,appsplit=True)
        self.assertEqual(startRef, ret) 


        top = filesysobjects.FileSysObjects.normpathX('/hostname')
        topRef = [('LFSYS', '', '', filesysobjects.FileSysObjects.normpathX('/hostname'))]
        ret = filesysobjects.FileSysObjects.splitPathVar(top,appsplit=True)
        self.assertEqual(topRef, ret) 


        top0ref=filesysobjects.FileSysObjects.normpathX('//hostname/tests/a/b/hostname')
        topRef = [('SHARE', 'hostname', 'tests', filesysobjects.FileSysObjects.normpathX('a/b/hostname'))]
        top = filesysobjects.FileSysObjects.getTopFromPathString(top, [start])
        ret = filesysobjects.FileSysObjects.splitPathVar(top,appsplit=True)

        self.assertEqual(top0ref, top) 
        self.assertEqual(topRef, ret) 
        pass

    def testCase030(self):
        
        start = filesysobjects.FileSysObjects.normpathX('//hostname/hostname/tests//////a/b/hostname//c////////d/tests/b///c')
        startRef = [('SHARE', 'hostname', 'hostname', filesysobjects.FileSysObjects.normpathX('tests/a/b/hostname/c/d/tests/b/c'))]
        ret = filesysobjects.FileSysObjects.splitPathVar(start,appsplit=True)
        self.assertEqual(startRef, ret) 

        top = filesysobjects.FileSysObjects.normpathX('/hostname')
        topRef = [('LFSYS', '', '', filesysobjects.FileSysObjects.normpathX('/hostname'))]
        ret = filesysobjects.FileSysObjects.splitPathVar(top,appsplit=True)
        self.assertEqual(topRef, ret) 


    def testCase040(self):
        
        start = 'smb://'+filesysobjects.FileSysObjects.normpathX('hostname/hostname/tests//////a/b/hostname//c////////d/tests/b///c')
        startRef = [('SMB', 'hostname', 'hostname', filesysobjects.FileSysObjects.normpathX('tests/a/b/hostname/c/d/tests/b/c'))]
        ret = filesysobjects.FileSysObjects.splitPathVar(start,appsplit=True)
        self.assertEqual(startRef, ret) 

        top = filesysobjects.FileSysObjects.normpathX('/hostname')
        topRef = [('LFSYS', '', '', filesysobjects.FileSysObjects.normpathX('/hostname'))]
        ret = filesysobjects.FileSysObjects.splitPathVar(top,appsplit=True)
        self.assertEqual(topRef, ret) 

        top0ref='smb://'+filesysobjects.FileSysObjects.normpathX('hostname/hostname/tests/a/b/hostname')
        topRef = [('SMB', 'hostname', 'hostname', filesysobjects.FileSysObjects.normpathX('tests/a/b/hostname'))]
        top = filesysobjects.FileSysObjects.getTopFromPathString(top, [start])
        ret = filesysobjects.FileSysObjects.splitPathVar(top,appsplit=True)

        self.assertEqual(top0ref, top) 
        self.assertEqual(topRef, ret) 
        pass


#
#######################
#

if __name__ == '__main__':
    unittest.main()

