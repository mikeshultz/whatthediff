# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatthedoc', '0004_webdocumentbody_body_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webdocumentbody',
            name='web_document',
            field=models.ForeignKey(to='whatthedoc.WebDocument', related_name='bodies'),
        ),
    ]
