from django.utils.translation import ugettext as _
from django.db import models

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
    
class WebDocumentBody(models.Model):
    document_body_id = models.AutoField(primary_key=True)
    web_document = models.ForeignKey(WebDocument, null=False)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Document Body')
        verbose_name_plural = _('Document Bodys')

    def __unicode__(self):
        pass
    