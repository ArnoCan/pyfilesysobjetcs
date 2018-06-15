from __future__ import absolute_import

import unittest
import os,sys

import filesysobjects.apppaths
from filesysobjects import RTE, RTE_WIN32

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"


#
#######################
#


class CallUnits(unittest.TestCase):

    def testCase000(self):
        apstr = filesysobjects.paths.normpathx('a:/')
        apstr += ";" + "b:/"
        apstr += ";" + filesysobjects.paths.normpathx('c:/')
        apstr += ";" + "d:/"
        apstr += ";" + filesysobjects.paths.normpathx('e:/')
        apstr += ";" + "f:/"
        apstr += ';abc;x:/we'

        if RTE & RTE_WIN32:
            retRef = [
                ('ldsys', '', 'a:', '\\'),
                ('ldsys', '', 'b:', '\\'),
                ('ldsys', '', 'c:', '\\'),
                ('ldsys', '', 'd:', '\\'),
                ('ldsys', '', 'e:', '\\'),
                ('ldsys', '', 'f:', '\\'),
                ('lfsys', '', '', 'abc'),
                ('ldsys', '', 'x:', '\\we')
            ]
        else:
            retRef =  [
                ('ldsys', '', 'a:', '/'),
                ('ldsys', '', 'b:', '/'),
                ('ldsys', '', 'c:', '/'),
                ('ldsys', '', 'd:', '/'),
                ('ldsys', '', 'e:', '/'),
                ('ldsys', '', 'f:', '/'),
                ('lfsys', '', '', 'abc'),
                ('ldsys', '', 'x:', '/we')
            ]

        ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True,spf='win',strict=True)
        self.assertEqual(retRef, ret)


#
#######################
#

if __name__ == '__main__':
    unittest.main()
