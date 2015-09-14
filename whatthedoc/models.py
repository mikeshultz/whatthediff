import hashlib
from datetime import datetime

from django.utils.translation import ugettext as _
from django.dispatch import receiver
from django.db import models, IntegrityError
from django.db.models.signals import post_save, pre_save
from whatthedoc.utils import FetchDocument

import logging
logger = logging.getLogger(__name__)

class WebDocumentDuplicate(IntegrityError): pass

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
    web_document = models.ForeignKey(WebDocument, null=False, related_name='bodies')
    body = models.TextField()
    body_hash = models.CharField(unique=True, max_length=32)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Document Body')
        verbose_name_plural = _('Document Bodys')

    def __unicode__(self):
        pass

@receiver(pre_save, sender=WebDocumentBody)
def create_web_document_body(sender, instance, **kwargs):
    "Need to handle some things when we first create a document."

    http_doc = FetchDocument(instance.web_document.url)
    #logger.debug('whatthedoc.models:55: Body: %s' % http_doc.body)
    
    if http_doc.body:
        # make md5 hash of body
        m = hashlib.md5()
        #body = http_doc._soup.get_text()
        #print('body: ', http_doc.body.encode('utf-8'))
        m.update(bytes(http_doc.body, 'utf-8'))
        body_hash = m.hexdigest()

        logger.debug('whatthedoc.models:64: body_hash: %s' % body_hash)

        if body_hash:
            matches = WebDocumentBody.objects.filter(body_hash = body_hash).count()
            logger.debug('whatthedoc.models:68: matches: %s' % matches)
            if matches == 0:

                if not instance.web_document.title:
                    instance.web_document.title = http_doc.title
                if http_doc.response.getheader('Last-Modified'):
                    last_mod = datetime.strptime(http_doc.response.getheader('Last-Modified'), '%a, %d %b %Y %H:%M:%S GMT')
                    instance.web_document.http_last_modified = last_mod

                instance.body = http_doc.body.encode('utf-8')
                instance.body_hash = body_hash

                #instance.web_document.save()

                # I don't think this is necessary(or wanted) in pre_save
                #instance.save()

            else:
                logger.info('whatthedoc.models:86: Document has not been changed.')
                raise WebDocumentDuplicate('Document has not been changed because we already have it in the database.')
        else:
            logger.error('whatthedoc.models:88: Document could not be hashed.')
            raise ValueError('Document could not be hashed.  May be empty.')
    