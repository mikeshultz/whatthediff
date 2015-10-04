# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('whatthecollection', '0004_auto_20150930_0625'),
        ('whatthediff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InviteToken',
            fields=[
                ('invite_tokent_id', models.UUIDField(primary_key=True, serialize=False, editable=False, default=uuid.uuid4)),
                ('email', models.EmailField(max_length=254)),
                ('can_write', models.BooleanField(default=False)),
                ('collection', models.ForeignKey(to='whatthecollection.Collection')),
            ],
            options={
                'verbose_name': 'Invite Token',
                'verbose_name_plural': 'Invite Tokens',
            },
        ),
    ]
