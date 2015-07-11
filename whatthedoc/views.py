from django.shortcuts import render_to_response, get_object_or_404

from whatthedoc.models import WebDocument

def new_web_document(request):
    "Create a new Web Document"
    return render_to_response("new_web_document.html", {})

def web_document(rquest, web_document_id = None):
    "Display Document"
    
    doc = get_object_or_404(WebDocument, pk=web_document_id)

    return render_to_response("web_document.html", { 'document': doc, })