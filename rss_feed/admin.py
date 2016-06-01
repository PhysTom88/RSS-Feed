from django.contrib import admin

from .models import User, RssFeed

class UserAdmin(admin.ModelAdmin):
	fieldsets = [
	('User Name', {'fields': ['username']}),
	('Date Joined', {'fields': ['joined']})
	]
	list_display = ('username', 'joined')
	list_filter = ['joined']
	search_fields = ['username']


class RssFeedAdmin(admin.ModelAdmin):
	fieldsets = [
	('Name', {'fields': ['feed_name']}),
	('URL', {'fields': ['feed_url']})
	]
	list_display = ('feed_name', 'feed_url')
	search_fields = ['feed_name']


admin.site.register(User, UserAdmin)
admin.site.register(RssFeed, RssFeedAdmin)
