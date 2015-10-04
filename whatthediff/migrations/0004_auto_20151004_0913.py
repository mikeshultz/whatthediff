# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatthediff', '0003_auto_20151004_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitetoken',
            name='collection',
            field=models.ForeignKey(null=True, to='whatthecollection.Collection'),
        ),
    ]
