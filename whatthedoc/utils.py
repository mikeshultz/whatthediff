import urllib.request
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
        self._soup = BeautifulSoup(self.response.read(), 'html.parser')

        #print(response.read())
        #self.headers = response.getheaders()
        #print(self.headers)
        self.body = self.response.read()

        self.title = self._soup.title.string

    @property
    def title(self):
        "Return document title if it exists, otherwise, try and fetch."
        if not self.body:
            self._fetch()
        return self._title
    @title.setter
    def title(self, value):
        self._title = value
