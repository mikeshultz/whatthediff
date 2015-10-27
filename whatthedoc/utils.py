import urllib.request, html2text, gzip
from bs4 import BeautifulSoup
from chardet.universaldetector import UniversalDetector
from django.conf import settings

class FetchDocumentError(Exception): pass

class FetchDocument(object):
    """Get a document and the basic needed information."""
    def __init__(self, url):
        self.url = url
        self.response = None
        self._body = str()
        self._title = str()
        self._soup = None
        self.error = None

        if self.url:
            self._fetch()

    def _fetch(self):
        "Make the http request and store pertinent information"

        req = urllib.request.Request(
            self.url, 
            headers={
                'User-Agent' : "What The Diff/0.1",
                'Accept-encoding': 'gzip',
            }
        ) 
        self.response = urllib.request.urlopen(req)

        # deal with special encodings
        if self.response.info().get('Content-Encoding') == 'gzip':
            f = gzip.GzipFile(fileobj=self.response)
        else:
            f = self.response

        self._buf = f.read() 

        # Let's try, and hope, that we can detect the encoding here
        u = UniversalDetector()
        u.feed(self._buf)
        char_result = u.close()
        print('Detected encoding: %s' % char_result['encoding'])

        # Now cross your fingers and hope we can actually decode whatever
        # ridiculous encoding they used.
        try:
            self._raw = self._buf.decode(char_result['encoding']) #.encode('utf8')
            print("self._raw is type %s" % type(self._raw))
        except DecodeError:
            self.error = "Not able to deocde %s" % char_result['encoding']
            print(self.error)
            raise FetchDocumentError(self.error)

        self._soup = BeautifulSoup(self._raw, 'html.parser')
        
        # TODO: should set base url to the domain of self.url so images
        # will show up better
        self.body = html2text.html2text(self._raw)

        try:
            self.title = self._soup.title.string
        except AttributeError: 
            self.title = self.url

    @property
    def title(self):
        "Return document title if it exists, otherwise, try and fetch."
        if not self.body:
            self._fetch()
        return self._title
    @title.setter
    def title(self, value):
        self._title = value
