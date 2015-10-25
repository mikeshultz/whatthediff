# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatthediff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='whattheuser',
            name='is_admin',
            field=models.BooleanField(verbose_name='Is the user an admin?', default=False),
        ),
    ]
