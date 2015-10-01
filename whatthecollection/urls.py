from django.conf.urls import include, url
from whatthecollection import views

urlpatterns = [
    url(r'new/*', views.new_collection, name='new_collection'),
    url(r'edit', views.edit_collection, name='edit_collection'),
    url(r'rights/edit', views.edit_rights, name='edit_collection_rights'),
    url(r'rights/add', views.edit_rights, name='add_user_to_collection'),
    #url(r'(?P<web_document_id>[0-9]+)/*', views.web_document, name='web_document'),
    url(r'', views.collection_list, name='collection_list'),
]