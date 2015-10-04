# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatthediff', '0002_invitetoken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invitetoken',
            old_name='invite_tokent_id',
            new_name='invitetoken_id',
        ),
    ]
