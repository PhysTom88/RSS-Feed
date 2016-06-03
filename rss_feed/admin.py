from django.contrib import admin

from .models import UserProfile, RssFeed, Subscribe


class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User Name', {'fields': ['user']}),
        ('Date Joined', {'fields': ['joined']})
    ]
    list_display = ('user', 'joined')
    list_filter = ['joined']
    search_fields = ['user']


class RssFeedAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['feed_name']}),
        ('URL', {'fields': ['feed_url']})
    ]
    list_display = ('feed_name', 'feed_url')
    search_fields = ['feed_name']


class SubscribeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User', {'fields': ['user']}),
        ('Feed', {'fields': ['rss_feed']})
    ]
    list_display = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(RssFeed, RssFeedAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
