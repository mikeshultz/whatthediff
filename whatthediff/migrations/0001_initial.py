# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('whatthecollection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatTheUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('first_name', models.CharField(max_length=128, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=128, verbose_name='Last Name')),
                ('email', models.EmailField(unique=True, max_length=255, help_text='E-mail address', verbose_name='E-mail')),
            ],
            options={
                'db_table': 'whatthediff_user',
            },
        ),
        migrations.CreateModel(
            name='InviteToken',
            fields=[
                ('invitetoken_id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('email', models.EmailField(max_length=254)),
                ('can_write', models.BooleanField(default=False)),
                ('collection', models.ForeignKey(to='whatthecollection.Collection', null=True)),
            ],
            options={
                'verbose_name_plural': 'Invite Tokens',
                'verbose_name': 'Invite Token',
            },
        ),
    ]
