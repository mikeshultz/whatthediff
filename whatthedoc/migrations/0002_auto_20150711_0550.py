# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatthedoc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webdocument',
            name='http_last_modified',
            field=models.DateTimeField(null=True, default=None),
        ),
    ]
