"""Create a plist, find a matching relative filepathname in directory tree.

Calling elementary functions.

* **Data**:
  ::
  
    see 'testdata.examples'
  
  refer also to the manual `[filesystem-elements-as-objects] <path_syntax.html#filesystem-elements-as-objects>`_

* **Call**:
  ::


    # 1. find the requested entry
    rp = findRelPathInSearchPath("F[0-5]*",_plist)
   
* **Result**:
  ::

    expected = os.path.normpath(testdata.mypath+'/examples/a/b0/c/a/b0/F1')

"""
from __future__ import absolute_import
from __future__ import print_function
import filesysobjects

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__='af90cc0c-de54-4a32-becd-06f5ce5a3a75'

__docformat__ = "restructuredtext en"

import unittest
import os,sys

from filesysobjects.FileSysObjects import setUpperTreeSearchPath
from filesysobjects.FileSysObjects import findRelPathInSearchPath
from filesysobjects.FileSysObjects import clearPath

#
#######################
#

class UseCase(unittest.TestCase):
    
    def testCase000(self):
        _s = sys.path[:]

        import testdata
        import filesysobjects.FileSysObjects
          
        s = os.sep
        
        # start of upward search - file is converted into it's containing directory node
        any_sub_path = os.path.normpath('examples/a/b0/c/a/b0/c/F')
        spath  = testdata.mypath
        spath += s+ any_sub_path

        # check environment
        assert os.path.exists(spath)
                
        # store new search list, here without required sys.path
        _plist = []


        # 0. build a search path list - if not yet available
        #    adds each directory from spath to its matching 
        #    subnode  "a/b"
        #
        setUpperTreeSearchPath(spath,os.path.normpath('a/b0'), _plist)
        _plist_ref = [ # expected plist
            os.path.normpath(testdata.mypath+'/examples/a/b0/c/a/b0/c'),
            os.path.normpath(testdata.mypath+'/examples/a/b0/c/a/b0'),
            os.path.normpath(testdata.mypath+'/examples/a/b0/c/a'),
            os.path.normpath(testdata.mypath+'/examples/a/b0/c'),
            os.path.normpath(testdata.mypath+'/examples/a/b0'),
        ]
        assert _plist_ref == _plist 

        # 1. find the requested entry
        rp = findRelPathInSearchPath("F[0-5]*",_plist)
        expected = os.path.normpath(testdata.mypath+'/examples/a/b0/c/a/b0/F1')
        assert expected == rp 


    
#
#######################
#

if __name__ == '__main__':
    unittest.main()

