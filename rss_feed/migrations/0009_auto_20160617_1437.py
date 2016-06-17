# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_feed', '0008_auto_20160603_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('summary', models.TextField(verbose_name=b'article summary')),
                ('published_date', models.DateTimeField(verbose_name=b'date published')),
                ('url', models.URLField(unique=True)),
                ('rss_feed', models.ForeignKey(to='rss_feed.RssFeed')),
            ],
        ),
        migrations.RemoveField(
            model_name='favourites',
            name='description',
        ),
        migrations.RemoveField(
            model_name='favourites',
            name='name',
        ),
        migrations.RemoveField(
            model_name='favourites',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='favourites',
            name='rss_feed',
        ),
        migrations.AddField(
            model_name='favourites',
            name='article',
            field=models.ManyToManyField(to='rss_feed.Article'),
        ),
    ]
