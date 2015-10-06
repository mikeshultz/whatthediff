from django.conf.urls import include, url
#from django.contrib import admin
from whatthediff import views
from whatthecollection import urls as wtc_views
from whatthedoc import urls as wtd_views
from pagediff import urls as pd_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login', views.loginyo, name='login'),
    url(r'^logout', views.logoutyo, name='logout'),
    url(r'^register', views.register, name='register'),
    url(r'^invite/(?P<invitetoken_id>[A-Za-z\-0-9]{36})', views.invite, name='invite'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^collection/', include(wtc_views)),
    url(r'^document/', include(wtd_views)),
    url(r'^diff/', include(pd_views)),
]
