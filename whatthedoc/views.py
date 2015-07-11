from django.shortcuts import render_to_response, get_object_or_404

from whatthedoc.models import WebDocument, WebDocumentBody

def new_web_document(request):
    "Create a new Web Document"
    return render_to_response("new_web_document.html", {})

def web_document(request, web_document_id = None):
    "Display Document"
    
    doc = get_object_or_404(WebDocument, pk=web_document_id)
    bodies = WebDocumentBody.objects.filter(web_document=doc).order_by('-created')

    return render_to_response("web_document.html", 
        { 
            'document': doc, 
            'latest': bodies[0], 
            'bodies': bodies, 
        }
    )

def web_document_list(request):
    "Show documents in a list"
    docs = WebDocument.objects.all()

    return render_to_response("web_document_list.html", 
        { 
            'docs': docs, 
        }
    )