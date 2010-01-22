import unittest

from zope.component import getUtility, getUtilitiesFor
from pkg_resources import resource_string, resource_filename
from pydataportability.microformats.htmlparsers import HTML5LibParser
from pydataportability.microformats.base.interfaces import IHTMLParser,IMicroformatsParser

import pydataportability.microformats.hcard
import pydataportability.microformats.xfn

class Test(unittest.TestCase):


    def test_fromString(self):

        data = resource_string(__name__, 'mrtopf_tidy.html')
        parser = getUtility(IHTMLParser,name="html5lib")()
        mf = parser.fromString(data)
        mf.parse()
        
        self.failUnless(mf.microformats.has_key('xfn'), 'xfn microformat not found')
        self.failUnless(mf.microformats.has_key('hcard'), 'hcard microformat not found')

    def test_fromFile(self):
        parser = getUtility(IHTMLParser,name="html5lib")()
        mf = parser.fromFile(resource_filename(__name__, 'mrtopf.html'))
        mf.parse()
        
        self.failUnless(mf.microformats.has_key('xfn'), 'xfn microformat not found')
        self.failUnless(mf.microformats.has_key('hcard'), 'hcard microformat not found')

    def test_fromURL(self):
        parser = getUtility(IHTMLParser,name="html5lib")()
        mf = parser.fromURL('http://www.google.com/')
        mf.parse()
        
        self.failIf(mf.microformats.has_key('xfn'), 'xfn microformat found on google page')
        self.failIf(mf.microformats.has_key('hcard'), 'hcard microformat found on google page')
        
        mf2 = parser.fromURL('http://twitter.com/jack')
        mf2.parse()
        
        self.failUnless(mf2.microformats.has_key('xfn'), 'xfn microformat not found')
        self.failUnless(mf2.microformats.has_key('hcard'), 'hcard microformat not found')
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()