# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomepageLearnMoreLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.FloatField(default=0)),
                ('show', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('icon_image', models.ImageField(upload_to=b'homepage_learn_more_links')),
                ('url', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomepageSpotlightLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.FloatField(default=0)),
                ('show', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=b'homepage_spotlight_links')),
                ('url', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomepageTestimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.FloatField(default=0)),
                ('show', models.BooleanField(default=False)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
