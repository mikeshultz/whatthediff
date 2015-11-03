# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatthedoc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webdocumentbody',
            name='body_hash',
            field=models.CharField(max_length=32),
        ),
    ]
