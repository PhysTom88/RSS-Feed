# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_feed', '0004_subscribe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='rss_feed',
        ),
        migrations.AddField(
            model_name='subscribe',
            name='rss_feed',
            field=models.ManyToManyField(to='rss_feed.RssFeed'),
        ),
    ]
