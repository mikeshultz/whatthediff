from .models import CollectionUser

def user_collections(request):
    """ If the user is logged in, let's include their collections at all
        times.  Originally put into place for use in the add document 
        form.
    """
    if request.user.is_authenticated():
        return { 'user_collections': CollectionUser.objects.filter(user_id=request.user.id), }
    else:
        return {}