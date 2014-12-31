# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bfa_homepage', '0003_auto_20141230_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomepagePhotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.FloatField(default=0)),
                ('show', models.BooleanField(default=False)),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to=b'homepage_photos')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
