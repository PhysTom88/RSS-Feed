from django.conf.urls import url

from rss_feed.views import (HomeView, LoginView, RegisterView,
                            LogoutView, UserView)


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='landing'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^user/$', UserView.as_view(), name='user'),
]
