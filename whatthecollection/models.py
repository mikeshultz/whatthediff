from django.utils.translation import ugettext as _
from django.db import models

from whatthediff.models import WhatTheUser

class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = _('Collection')
        verbose_name_plural = _('Collections')

    def __unicode__(self):
        pass

class CollectionUser(models.Model):
    """ Association of a user to a collection """
    collection_user_id = models.AutoField(primary_key=True)
    collection = models.ForeignKey(Collection)
    user = models.ForeignKey(WhatTheUser)