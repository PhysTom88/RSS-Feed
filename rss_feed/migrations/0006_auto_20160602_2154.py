# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_feed', '0005_auto_20160602_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='user',
            field=models.ForeignKey(to='rss_feed.UserProfile', null=True),
        ),
    ]
