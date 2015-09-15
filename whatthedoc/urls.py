from django.conf.urls import include, url
from whatthedoc import views

urlpatterns = [
    url(r'new/*', views.new_web_document, name='new_web_document'),
    #url(r'(?P<web_document_id>[0-9]+)/*(?P<document_body_id>[0-9]*)/*', views.web_document, name='web_document'),
    url(r'(?P<web_document_id>[0-9]+)/*', views.web_document, name='web_document'),
    url(r'', views.web_document_list, name='web_document_list'),
]