from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .models import WebDocument, WebDocumentBody, WebDocumentDuplicate
from .forms import WebDocumentForm
from whatthecollection.models import CollectionUser

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
            collection_user = CollectionUser.objects.filter(user=request.user.id)

            if form.cleaned_data.get('collection_id'):
                log.info('whatthedoc.views:30: Filtering collections on collection_id of %s' % form.cleaned_data['collection_id'])
                collection_user = collection_user.filter(collection_id=form.cleaned_data['collection_id'])

            log.debug('whatthedoc.views:27: Saving a document to collection %s.' % collection_user[0].collection_id)
            form.instance.collection = collection_user[0].collection

            form.user = request.user

            # Attempt a save of the form
            try:
                form.save()
            except WebDocumentDuplicate:
                log.warning('whatthedoc.views:40: Document already exists in system.')
                log.debug('whatthedoc.views:43: DocumentUser instnace %s' % form.instance)

                # Get the duplicate body and let's reuse it
                body 

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
        try:
            revision = bodies[0]
        except IndexError:
            revision = None

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

    collection_id = request.GET.get('collection_id')

    collection_user = CollectionUser.objects.filter(user=request.user.id)

    if collection_id:
        log.debug('views.web_document_list:71: Filtering by collection_id = %s' % collection_id)
        collection_user = collection_user.filter(collection_id=collection_id)

    collection_user_ids = []
    if len(collection_user) > 0:
        # Put the IDs into  a sequence for later use
        for cu in collection_user:
            collection_user_ids.append(cu.collection_id)

        docs = WebDocument.objects.extra(
            select = {
                'latest': "SELECT created FROM whatthedoc_webdocumentbody swdb WHERE whatthedoc_webdocument.web_document_id = swdb.web_document_id ORDER BY created DESC LIMIT 1",
            }
        ).select_related('collection').filter(collection_id__in=collection_user_ids).order_by('-latest', '-modified', '-created')
    else:
        docs = None

    return render_to_response("web_document_list.html", 
        RequestContext(request, { 
            'document_active': True,
            'docs': docs, 
        })
    )
