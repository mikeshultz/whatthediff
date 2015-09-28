from django.utils.translation import ugettext as _
from django.db import models

from whatthediff.models import WhatTheUser

class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = _('Collection')
        verbose_name_plural = _('Collections')

    def __unicode__(self):
        pass

class CollectionUser(models.Model):
    """ Association of a user to a collection """
    collection_user_id = models.AutoField(primary_key=True)
    collection = models.ForeignKey(Collection, related_name='users')
    user = models.ForeignKey(WhatTheUser)
    default = models.BooleanField(default=False)