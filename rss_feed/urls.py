from django.conf.urls import url

from rss_feed.views import HomeView, LoginView, RegisterView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='landing'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
]
