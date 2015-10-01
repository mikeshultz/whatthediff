from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .models import Collection, CollectionUser
from .forms import CollectionForm, CollectionUserForm

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
        raise NotImplementedError('The ability to change rights for users has not yet been added.')
    
    return redirect('collection_list')

@login_required
def edit_collection(request):
    "Edit a collection"

    if request.POST:
        log.error("whatthcollection.views:56: NOT IMPLEMENTED!")
        raise NotImplementedError("The ability to change a collection's name has not yet been implemented.")
    
    return redirect('collection_list')

@login_required
def add_user_to_collection(request):
    """ Add a user with ro rights to a collection.  Basically what we're
        doing here is creating a new CollectionUser instance.  All we 
        need to begin with is an E-mail address.  Then either we can 
        find an existing user, or a registration token.  The registration
        token will have this association already handy for when the user
        finally comes to the site to register.
    """

    form = CollectionUserForm(request.POST)

    if form.is_valid():

        collection_id = form.cleaned_data.get('collection_id')
        email = form.cleaned_data.get('email')
        perms = form.cleaned_data.get('perms', 'ro')
        
        # simple rw/ro permissions
        if perms == 'rw':
            can_write = True
        else:
            can_write = False

        already_has_access = False

        # We need to check and make sure they have write access to this
        # collection before we allow them to add anyone else.  If not, 
        # silently fail them.
        check_cus = CollectionUser.objects.get(user=request.user, collection_id=collection_id, can_write=True)
        if len(check_cus) == 0:
            redirect('collection_list')

        if collection_id and email:
            collection_user = CollectionUser.objects.filter(user__email=email)

            # Let's see if they already have an entry first
            for cu in collection_user:
                if cu.collection_id == collection_id:
                    already_has_access = True
                    break

            target_user = collection_user[0].user

            if not already_has_access:
                # user is not assigned, let's make sure they exist
                if target_user.is_active():
                    # Well, let's make the assignment
                    collection = Collection.objects.get(pk=collection_id)
                    new_cu = CollectionUser.objects.create(user=target_user, collection=collection, can_write=can_write)
                else:
                    # TODO: build a token and send out 
                    raise NotImplementedError('Invitation token generation is not yet implemented.')

    redirect('collection_list')


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