import urllib.request
import html2text
from bs4 import BeautifulSoup

class FetchDocument(object):
    """Get a document and the basic needed information."""
    def __init__(self, url):
        self.url = url
        self.response = None
        #self.headers = dict()
        self._body = str()
        self._title = str()
        self._soup = None

        if self.url:
            self._fetch()

    def _fetch(self):
        "Make the http request and store pertinent information"

        self.response = urllib.request.urlopen(self.url)
        self._raw = self.response.read().decode('utf-8')
        self._soup = BeautifulSoup(self._raw, 'html.parser')
        
        # TODO: should set base url to the domain of self.url
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
