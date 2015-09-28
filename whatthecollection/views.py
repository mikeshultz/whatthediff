from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .models import Collection, CollectionUser
from .forms import CollectionForm

import logging
log = logging.getLogger(__name__)

@login_required
def new_collection(request):
    "Create a new collection"

    if request.POST and request.POST.get('name'):
        log.info('whatthcollection.views:12: Saving collection...')

        form = CollectionForm(request.POST)
        if form.is_valid():

            # First, create a new collection
            collection = form.save()
            log.info('whatthcollection.views:20: Saved collection.')

            # Now, we need to associate this user to a collection
            collection_user = CollectionUser.objects.create(user=request.user, collection=collection)
            collection_user.save()
            log.info('whatthcollection.views:20: Saved user assignment to collection.')

            return redirect('collection_list')

        else:
            log.warn('whatthcollection.views:33: Failed saving the collection because: %s', form.error)

    # TODO: The user should probably be notified, but really, it's only
    # a name field...
    log.warn('whatthcollection.views:31: Failed saving the collection, wtf.')
    return redirect('collection_list')
    #return render_to_response("new_collection.html", RequestContext(request, {}))

@login_required
def edit_rights(request):
    "Create a new collection"

    if request.POST:
        log.error("whatthcollection.views:46: NOT IMPLEMENTED!")
        raise NotImplementedError
    
    return redirect('collection_list')

@login_required
def collection_list(request):
    "Show collections in a list"

    collection_user = CollectionUser.objects.filter(user=request.user.id)

    # if the user doesn't have any collections yet, we need to create 
    # one and assign it to them.
    if not collection_user: 
        collection = Collection.objects.create()
        collection_user = CollectionUser.objects.create(
            collection = collection,
            user = request.user,
            default = True
        )

    return render_to_response("collection_list.html", 
        RequestContext(request, { 
            'collection_active': True,
            'collection_user': collection_user, 
        })
    )