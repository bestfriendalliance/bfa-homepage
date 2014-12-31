# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bfa_homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamPageTeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.FloatField(default=0)),
                ('show', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=80)),
                ('bio', models.TextField()),
                ('mugshot_image', models.ImageField(upload_to=b'teampage_mugshots')),
                ('homepage_url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
