from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from mailer import send_html_mail
from django.conf import settings

from whatthediff.models import WhatTheUser

@login_required
def dashboard(request):
    "Admin dashboard"
    if not request.user.is_admin:
        return redirect('home')

    return render_to_response("dashboard.html", 
        RequestContext(request, {})
    )

@login_required
def send_email(request):
    "Send an E-mail to users"
    if not request.user.is_admin:
        return redirect('home')

    if request.POST:
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        #print(render_to_string('email/invite.txt', {'domain': settings.DOMAIN, 'token': token, 'subject': subject}))
        msg_plain = render_to_string('email/announce.txt', {'message': message, 'subject': subject})
        msg_html = render_to_string('email/announce.html', {'message': message, 'subject': subject})

        # right now, this is just to send messages to all of the users
        users = WhatTheUser.objects.filter(email__isnull=False)
        recipients = [u.email for u in users]
        for u in users:
            send_html_mail(subject, msg_plain, msg_html, settings.DEFAULT_FROM_EMAIL, [u.email, ])
        
        return redirect('admin-dashboard')

        #try:
        #send_html_mail(subject, msg_plain, msg_html, settings.DEFAULT_FROM_EMAIL, recipients)
        #finally:
        #    return redirect('admin-dashboard')

    return render_to_response("send_email.html", 
        RequestContext(request, {})
    )