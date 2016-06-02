# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_feed', '0003_auto_20160601_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rss_feed', models.ForeignKey(to='rss_feed.RssFeed')),
                ('user', models.ForeignKey(to='rss_feed.UserProfile')),
            ],
        ),
    ]
