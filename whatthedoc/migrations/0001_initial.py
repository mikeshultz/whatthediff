# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebDocument',
            fields=[
                ('web_document_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=256)),
                ('url', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('http_last_modified', models.DateTimeField(default=None)),
            ],
            options={
                'verbose_name_plural': 'Web Documents',
                'verbose_name': 'Web Document',
            },
        ),
        migrations.CreateModel(
            name='WebDocumentBody',
            fields=[
                ('document_body_id', models.AutoField(primary_key=True, serialize=False)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('web_document_id', models.ForeignKey(to='whatthedoc.WebDocument')),
            ],
            options={
                'verbose_name_plural': 'Document Bodys',
                'verbose_name': 'Document Body',
            },
        ),
    ]
