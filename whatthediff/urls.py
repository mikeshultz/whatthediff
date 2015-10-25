from django.conf.urls import include, url
from django.contrib import admin
from whatthediff import views
from whatthecollection import urls as wtc_views
from whatthedoc import urls as wtd_views
from pagediff import urls as pd_views
from whattheadmin import urls as wta_views

urlpatterns = [
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^login', views.loginyo, name='login'),
    url(r'^logout', views.logoutyo, name='logout'),
    url(r'^register', views.register, name='register'),
    url(r'^invite/(?P<invitetoken_id>[A-Za-z\-0-9]{36})', views.invite, name='invite'),
    url(r'^collection/', include(wtc_views)),
    url(r'^document/', include(wtd_views)),
    url(r'^diff/', include(pd_views)),
    url(r'^wta/', include(wta_views)),
]
