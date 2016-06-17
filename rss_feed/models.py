from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    '''Model for user'''

    user = models.OneToOneField(User)
    joined = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.user.username


class RssFeed(models.Model):
    '''Model for defining rss feeds'''

    feed_name = models.CharField(max_length=100, unique=True)
    feed_url = models.URLField(unique=True)

    def __unicode__(self):
        return self.feed_name


class Article(models.Model):
    '''Model for storing articles'''

    rss_feed = models.ForeignKey(RssFeed, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    summary = models.TextField('article summary')
    published_date = models.DateTimeField('date published')
    url = models.URLField(unique=True)

    def __unicode__(self):
        return self.title


class Favourites(models.Model):
    '''Model for favourites'''

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=False, null=True)
    article = models.ManyToManyField(Article)


class Subscribe(models.Model):
    '''Model for linking users to rss feeds'''

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    rss_feed = models.ManyToManyField(RssFeed)
