from __future__ import absolute_import
from __future__ import print_function
from linecache import getline

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os,sys

import filesysobjects.pathtools
import pysourceinfo.helper


#
#######################
#


class CallUnits(unittest.TestCase):

    def __init__(self,*args,**kargs):
        """Creates search path list
        """
        super(CallUnits,self).__init__(*args,**kargs)    

        self._s = sys.path[:]

        # data
        import testdata.filesysobjects
        self.myBase = testdata.filesysobjects.mypath+os.sep+"findnodes"

        #
        # prefix from unchanged sys.path
        self.mySysPathPrefixRaw = pysourceinfo.helper.getpythonpath(__file__) #@UnusedVariable
        
        self.myTestPath0Rel = os.path.normpath('a/b/c/d/e/f/g/h')
        self.myTestPath1Rel = self.myTestPath0Rel +os.sep+ self.myTestPath0Rel
        self.myTestPath2Rel = self.myTestPath1Rel +os.sep+ self.myTestPath0Rel
        
        self.myTestPath0 = self.myBase+os.sep+self.myTestPath0Rel #@UnusedVariable
        self.myTestPath1 = self.myBase+os.sep+self.myTestPath1Rel #@UnusedVariable
        self.myTestPath2 = self.myBase+os.sep+self.myTestPath2Rel #@UnusedVariable

    def reset_sys_path(self):
        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(self._s)
    
    def testCase000(self):
       
        pxn = self.myTestPath2

        rpath = 'h'+os.sep
        plist = ''
        plist += self.myTestPath2[:-1]
        plist += os.pathsep + self.myTestPath1[:-1]
        plist += os.pathsep + self.myTestPath0[:-1]
        
        px = filesysobjects.pathtools.findrelpath_in_searchpath(rpath,plist,subsplit=True)

        self.reset_sys_path()

        self.assertEqual(px, pxn) 
        pass

    def testCase001(self):
       
        pxn = self.myTestPath1

        rpath = 'h'+os.sep
        plist = ''
        plist += os.pathsep + self.myTestPath1[:-1]
        plist += os.pathsep + self.myTestPath2[:-1]
        plist += os.pathsep + self.myTestPath0[:-1]
        
        px = filesysobjects.pathtools.findrelpath_in_searchpath(rpath,plist,subsplit=True)

        self.reset_sys_path()

        self.assertEqual(px, pxn) 
        pass

    def testCase002(self):
       
        pxn = self.myTestPath0

        rpath = 'h'+os.sep
        plist = ''
        plist += os.pathsep + self.myTestPath0[:-1]
        plist += os.pathsep + self.myTestPath1[:-1]
        plist += os.pathsep + self.myTestPath2[:-1]
        
        px = filesysobjects.pathtools.findrelpath_in_searchpath(rpath,plist,subsplit=True)

        self.reset_sys_path()

        self.assertEqual(px, pxn) 
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

