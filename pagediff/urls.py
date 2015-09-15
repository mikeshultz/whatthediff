from django.conf.urls import include, url
from pagediff import views

urlpatterns = [
    url(r'(?P<document_body_id1>[0-9]+)/(?P<document_body_id2>[0-9]+)/*', views.diff_web_document, name='diff_web_document'),
]