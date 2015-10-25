# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('collection_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Collections',
                'verbose_name': 'Collection',
            },
        ),
        migrations.CreateModel(
            name='CollectionUser',
            fields=[
                ('collection_user_id', models.AutoField(serialize=False, primary_key=True)),
                ('default', models.BooleanField(default=False)),
                ('can_write', models.BooleanField(default=False)),
                ('collection', models.ForeignKey(related_name='users', to='whatthecollection.Collection')),
            ],
        ),
    ]
