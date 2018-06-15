"""
#**************************************************************

Platform         : linux2
Version          : 2.7.5 (default, Nov  3 2014, 14:33:39) 
[GCC 4.8.3 20140911 (Red Hat 4.8.3-7)]
Version-Info     : sys.version_info(major=2, minor=7, micro=5, releaselevel='final', serial=0)

Description      : Results by normpathx - local
                   
#**************************************************************
"""

norm_result = [
#--- 0
    r'\w1\w1\w2',
    r'\w2\w1\w2',
    r'\\w3\\w1\\w2',
    r'\\w4\\w1\\w2',
    r'\\\w5\\\w1\\\w2',
#--- 5
    r'\\\w6\\\w1\\\w2',
    r'\\\\w7\\\\w1\\\\w2',
    r'\\\\w8\\\\w1\\\\w2',
    r'\\\\\w9\\\\\w1\\\\\w2',
    r'\\\\\w10\\\\\w1\\\\\w2',
#--- 10
    r'/w1/w1/w2',
    r'//w2/w1/w2',
    r'/w3/w1/w2',
    r'/w4/w1/w2',
    r'/w5/w1/w2',
#--- 15
    r'/w6/w1/w2',
    r'/w7/w1/w2',
    r'/w8/w1/w2',
    r'/w9/w1/w2',
    r'/w10/w1/w2',
#--- 20
    r'\/w1/\w1\/w2',
    r'\/w2/\w1\/w2',
    r'\\/w3\\/w1\\/w2',
    r'\\/w4\\/w1\\/w2',
    r'\\\/w5\\\/w1\\\/w2',
#--- 25
    r'\/w1/\w1\/w2',
    r'\/\/w2\/\/w1\/\/w2',
    r'\/\/\/\/w3\/\/\/\/w1\/\/\/\/w2',
    r'\/\/\/\/\w4\/\/\/\/\w1\/\/\/\/\w2',
    r'\/\/\/\/\/w5\/\/\/\/\/w1\/\/\/\/\/w2',
#--- 30
    r'\/w1/\w1\/w2',
    r'\/\/w2\/\/w1\/\/w2',
    r'\/\/\/\/w3\/\/\/\/w1',
    r'\/\/\/\/\w4\/\/\/w1',
    r'\/\/\/\/\/w5',
#--- 35
    r'\/w1/\w1\/w2',
    r'\\/\\/w2\\/\\/w1\\/\\/w2',
    r'\\/\\/\\/\\/w3\\/\\/\\/\\/w1',
    r'\\\/\\\/\\\/\\\/\\\w4\\\/\\\/\\\/\\\/\\\w1',
    r'\\\/\\\/\\\/\\\/\\\/w5',
#--- 40
    '\a',
    '\b',
    '\f',
    '\n',
    '\r',
#--- 45
    '\t',
    '\v',
    '\\a',
    '\\b',
    '\\f',
#--- 50
    '\\n',
    '\\r',
    '\\t',
    '\\v',
    '\\\a',
#--- 55
    '\\\b',
    '\\\f',
    '\\\n',
    '\\\r',
    '\\\t',
#--- 60
    '/\v',
    '/\a',
    '/\b',
    '/\f',
    '/\n',
#--- 65
    '/\r',
    '/\t',
    '/\v',
    '/\\a',
    '/\\b',
#--- 70
    '/\\f',
    '/\\n',
    '/\\r',
    '/\\t',
    '/\\v',
#--- 75
    '/\\\a',
    '/\\\b',
    '/\\\f',
    '/\\\n',
    '/\\\r',
#--- 80
    '/\\\t',
    '/\\\v',
    '\/\\a',
    '\/\\b',
    '\/\\f',
#--- 85
    '\/\\n',
    '\/\\r',
    '\/\\t',
    '\/\\v',
    '\\/\a',
#--- 90
    '\\/\b',
    '\\/\f',
    '\\/\n',
    '\\/\r',
    '\\/\t',
#--- 95
    '\\/\v',
    '\\\/a',
    '\\\/b',
    '\\\/f',
    '\\\/n',
#--- 100
    '\\\/r',
    '\\\/t',
    '\\\/v',
    '/\a/\b/\f/\n/\r/\t/\v',
    '\\a\\b\\f\\n\\r\\t\\v',
#--- 105
    '\\\a\\\b\\\f\\\n\\\r\\\t\\\v',
    '\\\\a\\\\b\\\\f\\\\n\\\\r\\\\t\\\\v',
    '//\a/\b/\f/\n/\r/\t/\v',
    '/\a/\b/\f/\n/\r/\t/\v',
    '/\a/\b/\f/\n/\r/\t/\v',
#--- 110
    '\"\"',
    '\\"\\"',
    '\\\"\\\"',
    '\\\\"\\\\"',
    '/"/"',
#--- 115
    '//"/"',
    '/"/"',
    '/"/"',
    '\:\:',
    '\\:\\:',
#--- 120
    '\\\:\\\:;',
    '\\\\:;\\\\:',
    '/:/:;',
    '//:;/:',
    '/:/::',
#--- 125
    '/:/:',
    '\ \ ',
    '\\ \\ ',
    '\\\ \\\ ',
    '\\\\ \\\\ ',
#--- 130
    '/ / ',
    '// / ',
    '/ / ',
    '/ / ',
    '\;\;',
#--- 135
    r'\\;\\;',
    r'\\\;\\\;',
    r'\\\\;\\\\;',
    '/;/;',
    '//;/;',
#--- 140
    '/;/;',
    '/;/;',
    r'\
',
    r'/\
',
    r'/\
/A/\
',
#--- 145
    r'/\
/A',
    r'/\
/A/\
/B\
',
    r'/\
/w0/\
/w1/\
',
    u'\u0041', # utf-16 'A'
    u'/\u0041/\u0042', # utf-16 '/A/B'
#--- 150
    u'//\u0041/\u0042', # utf-16 '/A/B'
    u'/\u0041/\u0042', # utf-16 '/A/B'
    u'/\u0041/\u0042', # utf-16 '/A/B'
    u'\\u0041\\u0042', # utf-16 '/A/B'
    u'\\\u0041\\\u0042', # utf-16 '/A/B'
#--- 155
    u'\\\\u0041\\\\u0042', # utf-16 '/A/B'
    '\041', # octal 'A'
    '/\041/\042', # octal '/A/B'
    '//\041/\042', # octal '/A/B'
    '/\041/\042', # octal '/A/B'
#--- 160
    '/\041/\042', # octal '/A/B'
    '\041', # octal 'A'
    '\\041\\042', # octal '\A\B'
    '\\041\042', # octal '\A\B'
    '\\\041\\\042', # octal '\A\B'
#--- 165
    '\\\\041\\\\042', # octal '\A\B'
    '\\\\\041\\\\\042', # octal '\A\B'
    '\x41', # hex 'A'
    '/\x41/\x42', # hex '/A/B'
    '//\x41/\x42', # hex '/A/B'
#--- 170
    '/\x41/\x42', # hex '/A/B'
    '/\x41/\x42', # hex '/A/B'
    '\\x41\\x42', # hex '\A\B'
    '\\\x41\\\x42', # hex '\A\B'
    '\\\\x41\\\\x42', # hex '\A\B'
#--- 175
    '\\\\\x41\\\\\x42', # hex '\A\B'
    '\\',
    '\\/\\',
    '\\/\\/\\',
    '\\/\\/\\/\\',
#--- 180
    '\\/\\/\\/\\/\\',
    '\\\\',
    '\\\\/\\\\',
    r'\\/\\/\\',
    r'\\/\\/\\/\\',
#--- 185
    r'\\/\\/\\/\\/\\',
    r'\/\\',
    r'\/\\/\\',
    r'\/\\/\\/\\',
    r'\/\\/\\/\\/\\',
#--- 190
    r'\/\\/\\/\\/\\/\\',
    '\\\\\\',
    '\\\\\\/\\\\\\',
    '\\\\\\/\\\\\\/\\\\',
    '\\\\\\/\\\\\\/\\\\\\/\\\\\\',
#--- 195
    '\\\\\\/\\\\\\/\\\\\\/\\\\\\/\\\\',
    '\\\\\\',
    '\\\\\\/\\\\',
    '\\\\\\/\\\\/\\\\',
    '\\\\\\/\\\\/\\\\/\\\\',
#--- 200
    '\\\\\\/\\\\/\\/\\\\/\\\\',
    '\"""\"""',
    '\\"""\\"""',
    '\\\"""\\\"""',
    '\\\\"""\\\\"""',
#--- 205
    '/"""/"""',
    '//"""/"""',
    '/"""/"""',
    '/"""/"""',
    "\'''\'''",
#--- 210
    "\\'''\\'''",
    "\\\'''\\\'''",
    "\\\\'''\\\\'''",
    "/'''/'''",
    "//'''/'''",
#--- 215
    "/'''/'''",
    "/'''/'''",
]
