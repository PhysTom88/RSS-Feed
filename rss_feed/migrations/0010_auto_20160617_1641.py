# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_feed', '0009_auto_20160617_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourites',
            name='user',
            field=models.OneToOneField(to='rss_feed.UserProfile'),
        ),
    ]
