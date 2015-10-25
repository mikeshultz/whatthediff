from django.conf.urls import include, url
from whattheadmin import views

urlpatterns = [
    url(r'email/send', views.send_email, name='admin-new-email'),
    url(r'', views.dashboard, name='admin-dashboard'),
]