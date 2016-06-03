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


class Favourites(models.Model):
    '''Model for favourites'''

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rss_feed = models.ForeignKey(RssFeed, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField('rss description')
    published_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.name


class Subscribe(models.Model):
    '''Model for linking users to rss feeds'''

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    rss_feed = models.ManyToManyField(RssFeed)
