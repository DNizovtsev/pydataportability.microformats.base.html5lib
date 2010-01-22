import html5lib
from html5lib import treebuilders

from zope.component import adapts
from zope.interface import implements

from pydataportability.microformats.base.interfaces import IHTMLNode, IHTMLParser
from pydataportability.microformats.base.parser import MicroformatsParser

from pydataportability.microformats.base.htmlparsers.beautifulsoup import BeautifulSoupHTMLNode

import urllib2

class HTML5LibParser(object):
    """an HTML Parser based on html5lib.
     Used beautifulsoup tree builder then it very similar on pydataportability.microformats.base.htmlparsers.beautifulsoup
    """
    implements(IHTMLParser)

    def __init__(self):
        """initialize this parser"""
        self.initialized = False
        self.soup = None

    def fromString(self,string,**kwargs):
        """returns a node from a string of HTML

        should return an IHTMLNode for the root element
        """
        parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("beautifulsoup"))
        self.soup = parser.parse(string)
        node = MicroformatsParser(self.soup,**kwargs)
        self.initialized = True
        return node

    def fromFile(self, filename, **kwargs):
        """open a file and parse the document"""
        parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("beautifulsoup"))
        fp = open(filename,"r")
        self.soup = parser.parse(fp)
        fp.close()
        node = MicroformatsParser(self.soup,**kwargs)
        self.initialized = True
        return node

    def fromURL(self, url, **kwargs):
        """reads an HTML document from an URL and parse it
        """
        parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("beautifulsoup"))
        page = urllib2.urlopen(url)
        self.soup = parser.parse(page)
        node = MicroformatsParser(self.soup,**kwargs)
        self.initialized = True
        return node


class HTML5LibNode(BeautifulSoupHTMLNode):
    """Simple use exists class BeautifulSoupHTMLNode)"""
    pass

