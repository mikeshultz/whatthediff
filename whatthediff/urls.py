from django.conf.urls import include, url
#from django.contrib import admin
from whatthediff import views
from whatthedoc import urls as wtd_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^document/', include(wtd_views)),
]
