from django.test import TestCase
from .models import WebDocument, WebDocumentBody

class WebDocumentTestCase(TestCase):
    def setUp(self):
        self.web_doc = WebDocument.objects.create(url="http://www.mikes.network/")

    def test_fetch(self):
        """Test basic Web document fetch"""
        bodys = WebDocumentBody.objects.filter(web_document=self.web_doc)
        self.assertEqual(len(bodys), 1)