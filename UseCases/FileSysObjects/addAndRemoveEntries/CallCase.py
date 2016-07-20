"""Create a plist, find a matching relative filepathname in directory tree.

Calling elementary functions.

* **Data**:
  ::
  
    see 'testdata.examples'
  
  refer also to the manual `[filesystem-elements-as-objects] <path_syntax.html#filesystem-elements-as-objects>`_

* **Call**:
  ::

    import testdata
    import filesysobjects.FileSysObjects
      
    # start of upward search - file is converted into it's containing directory node
    s = os.sep
    any_sub_path = os.path.normpath('examples/a/b0/c/a/b0/c/F')
    spath  = testdata.mypath
    spath += any_sub_path

    # Here an empty list is used for search only. The function adds 
    # entries to the provided list storage, thus e.g. to 'sys.path' too.
    _plist = []

    # 0. build a search path list - if not yet available
    #    adds each directory from spath to its matching 
    #    subnode  "a/b"
    #
    setUpperTreeSearchPath(spath,os.path.normpath('b/B.txt'), _plist)
    rp = findRelPathInSearchPath(spath,_plist)


    _addp = _plist_ref[-1]

    # 1. append an item       
    _px = addPathToSearchPath(_addp, _plist,**{'append':True})

    # 2. remove the item
    delPathFromSearchPath(_addp, _plist)

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

from filesysobjects.FileSysObjects import addPathToSearchPath
from filesysobjects.FileSysObjects import delPathFromSearchPath
from filesysobjects.FileSysObjects import setUpperTreeSearchPath
from filesysobjects.FileSysObjects import findRelPathInSearchPath
from filesysobjects.FileSysObjects import clearPath

#
#######################
#

class CallUnits(unittest.TestCase):
    
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
            os.path.normpath(testdata.mypath+'/examples/a'),
        ]
        assert _plist_ref[:-1] == _plist 

        # 1. append an item       
        _addp = _plist_ref[-1]
        _px = addPathToSearchPath(_addp, _plist,**{'append':True})
        assert _px == len(_plist_ref)-1 # here just a demo
        assert _plist_ref == _plist 

        # 2. remove the item
        _addp = _plist_ref[-1]
        delPathFromSearchPath(_addp, _plist)
        assert _plist_ref[:-1] == _plist 


    
#
#######################
#

if __name__ == '__main__':
    unittest.main()
