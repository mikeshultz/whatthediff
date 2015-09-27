# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatthedoc', '0007_webdocument_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectionuser',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='collectionuser',
            name='user',
        ),
        migrations.AlterField(
            model_name='webdocument',
            name='collection',
            field=models.ForeignKey(to='whatthecollection.Collection'),
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
        migrations.DeleteModel(
            name='CollectionUser',
        ),
    ]
