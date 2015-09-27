from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .models import Collection, CollectionUser

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