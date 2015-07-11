# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatthedoc', '0002_auto_20150711_0550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webdocumentbody',
            old_name='web_document_id',
            new_name='web_document',
        ),
    ]
