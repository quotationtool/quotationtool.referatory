import unittest
import doctest
import os.path
import zope.interface
import zope.component
from zope.component.testing import setUp, tearDown, PlacelessSetup
from zope.configuration.xmlconfig import XMLConfig

import quotationtool.referatory

def testZCML(test):
    """
        >>> import quotationtool.referatory
        >>> from zope.configuration.xmlconfig import XMLConfig
        >>> XMLConfig('configure.zcml', quotationtool.referatory)()

    """


def setUpZCML(test):
    setUp(test)
    XMLConfig('configure.zcml', quotationtool.referatory)()
    

def test_suite():
    return unittest.TestSuite((
            doctest.DocTestSuite('quotationtool.referatory.interfaces',
                                 setUp = setUpZCML,
                                 tearDown = tearDown,
                                 optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS,
                                 ),
            doctest.DocFileSuite('README.txt',
                                 setUp = setUpZCML,
                                 tearDown = tearDown,
                                 optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS),
            doctest.DocTestSuite(setUp = setUp, tearDown = tearDown),
            ))

