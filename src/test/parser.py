
from zope.component import getUtility, getUtilitiesFor

from pkg_resources import resource_string
import pydataportability.microformats.hcard
import pydataportability.microformats.xfn

from pydataportability.microformats.htmlparsers import HTML5LibParser
from pydataportability.microformats.base.interfaces import IHTMLParser,IMicroformatsParser

#data = resource_string(__name__, 'laibcoms_asia_blog.html')
data = resource_string(__name__, 'mrtopf_tidy.html')

parser = getUtility(IHTMLParser,name="html5lib")()
mf = parser.fromString(data)
mf.parse()


parsers = getUtilitiesFor(IMicroformatsParser)

for name,result in mf.microformats.items():
    print "**",name,"**"
    print result[0]
    for r in result:
        print r
