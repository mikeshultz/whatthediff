# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatthecollection', '0003_collection_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionuser',
            name='can_write',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='collectionuser',
            name='collection',
            field=models.ForeignKey(related_name='users', to='whatthecollection.Collection'),
        ),
    ]
