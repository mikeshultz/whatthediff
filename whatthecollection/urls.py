from django.conf.urls import include, url
from whatthecollection import views

urlpatterns = [
    #url(r'new/*', views.new_web_document, name='new_web_document'),
    #url(r'(?P<web_document_id>[0-9]+)/*', views.web_document, name='web_document'),
    url(r'', views.collection_list, name='collection_list'),
]