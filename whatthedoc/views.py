from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from .models import CollectionUser, WebDocument, WebDocumentBody
from .forms import WebDocumentForm

import logging
log = logging.getLogger(__name__)

def new_web_document(request):
    "Create a new Web Document"

    if request.POST and request.POST.get('url'):
        log.info('whatthedoc.views:12: Saving document...')

        form = WebDocumentForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            log.info('whatthedoc.views:21: Redirecting to %s.' % form.instance.get_absolute_url())
            return redirect(form.instance.get_absolute_url())

    return render_to_response("new_web_document.html", RequestContext(request, {}))

def web_document(request, web_document_id = None):
    "Display Document"

    document_body_id = request.GET.get('document_body_id')
    
    doc = get_object_or_404(WebDocument, pk=web_document_id) # how..., user=request.user)
    bodies = WebDocumentBody.objects.filter(web_document=doc).order_by('-created')

    if document_body_id:
        revision = bodies.get(pk=document_body_id)
    else:
        revision = bodies[0]

    log.debug('whatthedoc.views:25: %s' % revision)

    return render_to_response("web_document.html", 
        RequestContext(request, { 
            'document': doc, 
            'revision': revision,
            'bodies': bodies, 
        })
    )

def web_document_list(request):
    "Show documents in a list"

    collection_user = CollectionUser.objects.filter(user=request.user)

    if collection_user:
        docs = []
        for cu in collection_user:
            docs += WebDocument.objects.filter(collection=cu.collection)
    else:
        docs = None

    return render_to_response("web_document_list.html", 
        RequestContext(request, { 
            'docs': docs, 
        })
    )