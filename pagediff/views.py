import difflib, logging
from django.shortcuts import render_to_response, get_object_or_404

from whatthedoc.models import WebDocumentBody

log = logging.getLogger(__name__)

def diff_web_document(request, document_body_id1 = None, document_body_id2 = None):
    "Show the diff of two Web Documents"

    doc_body1 = get_object_or_404(WebDocumentBody, pk=document_body_id1)
    doc_body2 = get_object_or_404(WebDocumentBody, pk=document_body_id2)

    document = doc_body1.web_document

    diff = difflib.unified_diff(doc_body1.body.splitlines(), doc_body2.body.splitlines())

    return render_to_response("diff_web_document.html", 
        RequestContext(request, { 
            'document_body1': doc_body1, 
            'document_body2': doc_body2, 
            'diff': diff,
        })
    )