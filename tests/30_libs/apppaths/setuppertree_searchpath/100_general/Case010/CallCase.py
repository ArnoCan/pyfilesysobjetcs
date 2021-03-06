"""Pretty print self.data.
"""
from __future__ import absolute_import

import unittest
import os,sys

from filesysobjects.apppaths import set_uppertree_searchpath


#
#######################
#
class CallUnits(unittest.TestCase):
    

    
    

    #
    # Create by object
    #
    def testCase000(self):
        _s = sys.path[:]

        A = os.path.normpath('a/A.txt')         #@UnusedVariable
        B = os.path.normpath('a/b/B.txt')       #@UnusedVariable
        C = os.path.normpath('a/b/c/C.txt')     #@UnusedVariable
        D = os.path.normpath('a/b/c/d/D.txt')   #@UnusedVariable

        top = os.path.abspath(os.path.dirname(__file__))  #@UnusedVariable
        start = top+os.sep+A

        res = []
        ret = set_uppertree_searchpath(start,top,res) #@UnusedVariable
        
        resx = [
            os.path.dirname(top+os.sep+A),
            top,
        ]

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)
        

        assert resx == res
        pass

    def testCase001(self):
        _s = sys.path[:]

        A = os.path.normpath('a/A.txt')         #@UnusedVariable
        B = os.path.normpath('a/b/B.txt')       #@UnusedVariable
        C = os.path.normpath('a/b/c/C.txt')     #@UnusedVariable
        D = os.path.normpath('a/b/c/d/D.txt')   #@UnusedVariable

        top = os.path.abspath(os.path.dirname(__file__))
        start = top+os.sep+B

        res = []
        ret = set_uppertree_searchpath(start,top,res) #@UnusedVariable
        
        resx = [
            os.path.dirname(top+os.sep+B),
            top,
        ]
        resx.insert(1,os.path.dirname(resx[0][:-1]))

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)
        

        assert resx == res
        pass

    def testCase002(self):
        _s = sys.path[:]

        A = os.path.normpath('a/A.txt')         #@UnusedVariable
        B = os.path.normpath('a/b/B.txt')       #@UnusedVariable
        C = os.path.normpath('a/b/c/C.txt')     #@UnusedVariable
        D = os.path.normpath('a/b/c/d/D.txt')   #@UnusedVariable

        top = os.path.abspath(os.path.dirname(__file__))
        start = top+os.sep+C

        res = []
        ret = set_uppertree_searchpath(start,top,res) #@UnusedVariable
        
        resx = [
            os.path.dirname(top+os.sep+C),
            top,
        ]
        resx.insert(1,os.path.dirname(resx[0][:-1]))
        resx.insert(2,os.path.dirname(resx[1][:-1]))

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)
        

        assert resx == res
        pass

    def testCase003(self):
        _s = sys.path[:]

        A = os.path.normpath('a/A.txt')         #@UnusedVariable
        B = os.path.normpath('a/b/B.txt')       #@UnusedVariable
        C = os.path.normpath('a/b/c/C.txt')     #@UnusedVariable
        D = os.path.normpath('a/b/c/d/D.txt')   #@UnusedVariable

        top = os.path.abspath(os.path.dirname(__file__))
        start = top+os.sep+D

        res = []
        ret = set_uppertree_searchpath(start,top,res) #@UnusedVariable
        
        resx = [
            os.path.dirname(top+os.sep+D),
            top,
        ]
        resx.insert(1,os.path.dirname(resx[0][:-1]))
        resx.insert(2,os.path.dirname(resx[1][:-1]))
        resx.insert(3,os.path.dirname(resx[2][:-1]))

        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(_s)
        

        assert resx == res
        pass

if __name__ == '__main__':
    unittest.main()
