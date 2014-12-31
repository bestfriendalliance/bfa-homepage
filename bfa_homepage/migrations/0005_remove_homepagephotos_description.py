# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bfa_homepage', '0004_homepagephotos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagephotos',
            name='description',
        ),
    ]
