# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bfa_homepage', '0002_teampageteammember'),
    ]

    operations = [
        migrations.AddField(
            model_name='teampageteammember',
            name='twitter_url',
            field=models.URLField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teampageteammember',
            name='homepage_url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
