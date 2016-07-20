filesysobjects
==============

The 'filesysobjects' package provides utilities for the application of
basic object oriented features onto filesystems.
This includes basic coverage of the 'inspect' package for the simplified
gathering of information on packages, modules, and files.

The provided feature modules comprise the following list.
For code examples refer to 'filesysobjects.UseCases'.

The package 'filesysobjects' is a spin off from the project 'UnifiedSessionsManager-2.0',
see 'https://sourceforge.net/projects/ctys/'.

The main interface classes are:

* **FileSysObjects** - Filesystem objects.

For UseCases refer to subdirectory:

* UseCases
 
**Downloads**:

* Sourceforge.net: https://sourceforge.net/projects/pyfilesysobjetcs/files/
  
* Sourceforge.net: https://sourceforge.net/projects/pyfilesysobjects/files/

* Github: https://github.com/ArnoCan/pyfilesysobjects/

**Online documentation**:

* https://pypi.python.org/pypi/pyfilesysobjects/
* https://pythonhosted.org/pyfilesysobjects/

setup.py
--------

The installer adds a few options to the standard setuptools options.

* *build_sphinx*: Creates documentation for runtime system by Sphinx, html only. Calls 'callDocSphinx.sh'.

* *build_epydoc*: Creates documentation for runtime system by Epydoc, html only. Calls 'callDocEpydoc.sh'.

* *instal_doc*: Install a local copy of the previously build documents in accordance to PEP-370.

* *test*: Runs PyUnit tests by discovery.

* *--help-filesysobjects*: Displays this help.

* *--no-install-required*: Suppresses installation dependency checks, requires appropriate PYTHONPATH.

* *--offline*: Sets online dependencies to offline, or ignores online dependencies.

* *--exit*: Exit 'setup.py'.

After successful installation the 'selftest' verifies basic checks by:

  *filesysobjects --selftest*

with the exit value '0' when OK.

The option '-v' raises the degree of verbosity for inspection

  *filesysobjects --selftest -v -v -v -v*
 

Project Data
------------

* PROJECT: 'filesysobjects'

* MISSION: Extend the standard PyUnit package for arbitrary ExecUnits.

* VERSION: 00.01

* RELEASE: 00.01.004

* NICKNAME: 'Yggdrasil'

* STATUS: alpha

* AUTHOR: Arno-Can Uestuensoez

* COPYRIGHT: Copyright (C) 2010,2011,2015-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez

* LICENSE: Artistic-License-2.0 + Forced-Fairplay-Constraints
  Refer to enclose documents:
  
  *  ArtisticLicense20.html - for base license: Artistic-License-2.0 

  *  licenses-amendments.txt - for amendments: Forced-Fairplay-Constraints

VERSIONS and RELEASES
---------------------

**Planned Releases:**

* RELEASE: 00.00.00x - Pre-Alpha: Extraction of the features from hard-coded application into a reusable package.

* RELEASE: 00.01.00x - Alpha: Completion of basic features. 

* RELEASE: 00.02.00x - Alpha: Completion of features, stable interface. 

* RELEASE: 00.03.00x - Beta: Accomplish test cases for medium to high complexity.

* RELEASE: 00.04.00x - Production: First production release. Estimated number of UnitTests := 250.

* RELEASE: 00.05.00x - Production: Various performance enhancements.


**Current Release: 00.01.005 - Alpha:**

OS-Support - Tested by PyUnit/Eclipse with Success:

* Linux: Fedora - others should work, ToDo: CentOS, Debian, and SuSE 

* Windows: Win10 - others see Cygwin

* Mac-OS: Snow Leopard - others should work

* Cygwin: 2.874/64 bit


OS-Support - ToDo: Going to follow soon.

* BSD: ToDo: OpenBSD, FreeBSD - others should work

* UNIX: ToDo: Solaris-11 - should work


Major Changes:

* Dropped 'findRelPathInUpperTree', is provided by others

* Minor fixes

* Added some UseCases for glob input/output

* Changed to absolute paths of subcalls of pzsourceinfo for platform independency

**ToDo**:

* Full scale UNC

* Fix bugs in SMB share conversion 

* Test for remote and autonomous operations on arbitrary filesystems 

Known Issues:

* Some minor failures of units, 1 on MacOS, will be fixed for a.s.a.p. 

Current test status:

* UnitTests: >580

* Use-Cases as UnitTests: >110

**Total**: >690

