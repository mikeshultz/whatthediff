# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatthecollection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebDocument',
            fields=[
                ('web_document_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=256, default='')),
                ('url', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('http_last_modified', models.DateTimeField(default=None, null=True)),
                ('collection', models.ForeignKey(to='whatthecollection.Collection')),
            ],
            options={
                'verbose_name_plural': 'Web Documents',
                'verbose_name': 'Web Document',
            },
        ),
        migrations.CreateModel(
            name='WebDocumentBody',
            fields=[
                ('document_body_id', models.AutoField(serialize=False, primary_key=True)),
                ('body', models.TextField()),
                ('body_hash', models.CharField(max_length=32, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('web_document', models.ForeignKey(related_name='bodies', to='whatthedoc.WebDocument')),
            ],
            options={
                'verbose_name_plural': 'Document Bodys',
                'verbose_name': 'Document Body',
            },
        ),
    ]
