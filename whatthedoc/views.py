from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .models import CollectionUser, WebDocument, WebDocumentBody
from .forms import WebDocumentForm

import logging
log = logging.getLogger(__name__)

@login_required
def new_web_document(request):
    "Create a new Web Document"

    if request.POST and request.POST.get('url'):
        log.info('whatthedoc.views:12: Saving document...')

        form = WebDocumentForm(request.POST)
        if form.is_valid():

            # get the collection for the user to add the document to
            # for now, we're assuming one election per user
            #
            # TODO: Breakout collections a bit more for the user so other
            #       users can be given access to a collection.
            collection_user = CollectionUser.objects.filter(user=request.user.id)[0]
            log.debug('whatthedoc.views:27: Saving a document to collection %s.' % collection_user.collection_id)
            form.instance.collection = collection_user.collection

            form.user = request.user
            form.save()
            log.info('whatthedoc.views:21: Redirecting to %s.' % form.instance.get_absolute_url())
            return redirect(form.instance.get_absolute_url())

    return render_to_response("new_web_document.html", RequestContext(request, {}))

@login_required
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

@login_required
def web_document_list(request):
    "Show documents in a list"

    collection_user = CollectionUser.objects.filter(user=request.user.id)

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