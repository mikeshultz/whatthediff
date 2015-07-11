from django.test import TestCase
from .models import WebDocument, WebDocumentBody

class WebDocumentTestCase(TestCase):
    def setUp(self):
        doc = WebDocument.objects.create(title="Test Document One", url="http://localhost/dafuq")
        body1 = """
Shotty to the body.
"""
        body2 = """
"Shotty to the body." - McPotty
"""
        WebDocumentBody.objects.create(web_document = doc, body=body1)
        WebDocumentBody.objects.create(web_document = doc, body=body2)

    def test_document_basic(self):
        """Test out basic documents."""
        doc = WebDocument.objects.get(web_document_id = 1)
        all_bodys = WebDocumentBody.objects.filter(web_document_id = doc.web_document_id).order_by('-created')

        print("First: ", all_bodys[0].created)
        print("Second: ", all_bodys[1].created)
        
        self.assertGreater(all_bodys[0].created, all_bodys[1].created)
        self.assertEqual(all_bodys[0].web_document, all_bodys[1].web_document)