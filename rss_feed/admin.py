from django.contrib import admin

from .models import UserProfile, RssFeed


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


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(RssFeed, RssFeedAdmin)
