# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatthedoc', '0003_auto_20150711_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='webdocumentbody',
            name='body_hash',
            field=models.CharField(max_length=32, default='xxxxx', unique=True),
            preserve_default=False,
        ),
    ]
