# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WhatTheUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('first_name', models.CharField(verbose_name='First Name', max_length=128)),
                ('last_name', models.CharField(verbose_name='Last Name', max_length=128)),
                ('email', models.EmailField(help_text='E-mail address', unique=True, verbose_name='E-mail', max_length=255)),
            ],
            options={
                'db_table': 'whatthediff_user',
            },
        ),
    ]
