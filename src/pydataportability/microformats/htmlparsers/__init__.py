from zope.component import provideUtility, provideAdapter
from pydataportability.microformats.base.interfaces import IHTMLParser, IHTMLNode

from html5libparser import HTML5LibParser, HTML5LibNode


provideUtility(HTML5LibParser, IHTMLParser, name="html5lib")

provideAdapter(HTML5LibNode)
