# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rss_feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
