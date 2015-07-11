import hashlib
from datetime import datetime

from django.utils.translation import ugettext as _
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_save
from whatthedoc.utils import FetchDocument

class WebDocument(models.Model):
    web_document_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, default='')
    url = models.URLField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    http_last_modified = models.DateTimeField(null=True, default=None)

    class Meta:
        verbose_name = _('Web Document')
        verbose_name_plural = _('Web Documents')

    def __unicode__(self):
        return self.url

@receiver(post_save, sender=WebDocument)
def create_web_document(sender, instance, created, **kwargs):
    "Need to handle some things when we first create a document."
    if created: 
        WebDocumentBody.objects.create(web_document = instance)
    
class WebDocumentBody(models.Model):
    document_body_id = models.AutoField(primary_key=True)
    web_document = models.ForeignKey(WebDocument, null=False)
    body = models.TextField()
    body_hash = models.CharField(unique=True, max_length=32)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Document Body')
        verbose_name_plural = _('Document Bodys')

    def __unicode__(self):
        pass

@receiver(post_save, sender=WebDocumentBody)
def create_web_document_body(sender, instance, created, **kwargs):
    "Need to handle some things when we first create a document."
    if created: 
        http_doc = FetchDocument(instance.web_document.url)
        last_mod = datetime.strptime(http_doc.response.getheader('Last-Modified'), '%a, %d %b %Y %H:%M:%S GMT')
        
        # make md5 hash of body
        m = hashlib.md5()
        body = http_doc._soup.get_text()
        m.update(bytes(body, 'utf-8'))
        body_hash = m.digest().decode('utf-16')

        if not instance.web_document.title:
            instance.web_document.title = http_doc.title
        instance.web_document.http_last_modified = last_mod
        instance.web_document.save()
        
        instance.body = body
        instance.body_hash = body_hash

        instance.save()
    