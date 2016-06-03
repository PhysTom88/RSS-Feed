from .models import RssFeed, Subscribe

import feedparser


def get_rss_feeds(request):

    fields = ['title', 'published', 'summary', 'url']
    feeds_detail = {}
    if request.user.is_authenticated():
        feeds = Subscribe.objects.get(user=request.user).rss_feed.all()
    else:
        feeds = RssFeed.objects.all()
    for feed in feeds:
        fp = feedparser.parse(feed.feed_url)
        feed_article = {}
        for i, article in enumerate(fp.entries, 1):
            values = [article['title_detail']['value'],
                      article['published'], article['summary_detail']['value'],
                      article['link']]

            feed_article[i] = dict(zip(fields, values))

        feeds_detail[feed.feed_name] = feed_article

    return feeds_detail
