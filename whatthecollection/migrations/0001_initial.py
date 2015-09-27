# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('collection_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.CreateModel(
            name='CollectionUser',
            fields=[
                ('collection_user_id', models.AutoField(serialize=False, primary_key=True)),
                ('collection', models.ForeignKey(to='whatthecollection.Collection')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
