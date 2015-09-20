# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatthedoc', '0006_collection_collectionuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='webdocument',
            name='collection',
            field=models.ForeignKey(default=1, to='whatthedoc.Collection'),
            preserve_default=False,
        ),
    ]
