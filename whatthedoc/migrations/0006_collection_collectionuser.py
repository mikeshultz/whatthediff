# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whatthedoc', '0005_auto_20150912_0706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('collection_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.CreateModel(
            name='CollectionUser',
            fields=[
                ('collection_user_id', models.AutoField(primary_key=True, serialize=False)),
                ('collection', models.ForeignKey(to='whatthedoc.Collection')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
