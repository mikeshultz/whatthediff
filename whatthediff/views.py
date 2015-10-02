from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from .models import WhatTheUser
from .forms import RegistrationForm

import logging
log = logging.getLogger(__name__)

def home(request):
    "Homepage"
    return render_to_response("home.html", RequestContext(request, {}))

def loginyo(request): 
    """ Simple user login """

    error = None
    email = request.POST.get('email')
    password = request.POST.get('password')

    if request.POST:

        if email and password:

            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    error = "The account has been disabled!  Please <a href=\"{% url 'contact' %}\">contact us for help resolving this issue."
                    log.info('whatthediff.views:27: User login attempt for %s shows user is disabled.' % email)
            else:
                error = "The E-mail and/or password are incorrect."
                log.info('whatthediff.views:30: Failed login attempt for %s' % email)

        else:
            error = "You must provide an E-mail address and password."

    return render_to_response("login.html", RequestContext(request, {'email': email, 'error': error, }))

def logoutyo(request):
    """ Terminate a session """
    logout(request)
    return redirect('home')

def user(request, user = None):
    """ General user page """

    if user:
        user = get_object_or_404(WhatTheUser, username=user)
        return redirect('home')

    # TODO: will want settings here eventually, but let's just go home for now
    return redirect('login')

def register(request):
    """ Register a user """

    if request.POST:
        log.info('whatthediff.views:62: register()')

        form = RegistrationForm(request.POST)
        if form.is_valid():
            log.info('whatthediff.views:67: Form is valid.')
            form.save()

            # Let's make it easy(for now, anyway), and log them right in.
            log.info('whatthediff.views:71: Logging the user in')

            new_user = authenticate(username=request.POST['email'], password=request.POST.get('password1'))
            login(request, new_user)

            return redirect('home')

            # TODO: Send activation E-mail and all that jazz
        else:
            log.warning('whatthediff.views:76: Form is not valid')
            log.debug(form.errors)

    else:
        form = RegistrationForm()

    return render_to_response("register.html", RequestContext(
            request, 
            {
                'form': form, 
            }
        )
    )

