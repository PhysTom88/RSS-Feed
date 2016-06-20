from django.contrib.auth import authenticate, login, logout, decorators
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import generic

from .forms import UserForm, RssSubscribeForm, FavouriteForm
from .models import UserProfile, RssFeed, Subscribe, Article, Favourites
from .rss_feed import get_rss_feeds

from datetime import datetime


class HomeView(generic.View):
    '''View for home page

       Displays current list of rss with option to
       favourite a selection
    '''

    def post(self, request):
        feeds = self.get_user_feeds(request)
        favourite_form = FavouriteForm(request.POST, feeds=feeds)
        if favourite_form.is_valid():
            faves = favourite_form.save()
            faves.user = request.user
            for article in request.POST.getlist('add_to_favourites'):
                faves.article.add(Article.objects.get(pk=article))
            faves.save()

            return redirect('main:landing')
        else:
            return render(
                request, 'favourite.html', {'fav_form': favourite_form})

    def get(self, request):
        feeds = get_rss_feeds(request)

        for feed, values in feeds.iteritems():
            rss_feed = RssFeed.objects.get(feed_name=feed)
            for i, info in feeds[feed].iteritems():
                try:
                    Article.objects.get(url=info['url'])
                except ObjectDoesNotExist:
                    a = Article(rss_feed=rss_feed, title=info['title'],
                                summary=info['summary'],
                                published_date=datetime.strptime(
                                    info['published'],
                                    '%a, %d %b %Y %H:%M:%S %Z'),
                                url=info['url'])
                    a.save()

        if request.user.is_authenticated():
            articles = self.get_user_feeds(request)
            fav_form = FavouriteForm(feeds=articles)
            return render(request, 'favourite.html', {'fav_form': fav_form})
        else:
            return render(request, 'home.html', {'feeds': feeds})

    def get_user_feeds(self, request):
        subscribe = Subscribe.objects.get(user=request.user).rss_feed.all()
        favourites = Favourites.objects.filter(
            user=request.user).values_list('article__pk', flat=True)
        articles = Article.objects.filter(
            rss_feed__in=subscribe).order_by('-published_date').exclude(
            pk__in=favourites)

        return articles


class LoginView(generic.View):

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,
                            password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('main:landing')
            else:
                message = "user is disabled!"
                return render(request, 'login/login.html',
                              {'message': message})
        else:
            message = "Username and password do not match any records"
            return render(request, 'login/login.html',
                          {'message': message})

    def get(self, request):
        return render(request, 'login/login.html', {'message': ''})


class RegisterView(generic.View):

    def post(self, request):
        user_form = UserForm(request.POST)
        rss_form = RssSubscribeForm(request.POST)
        if user_form.is_valid() and rss_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.username = user.email
            user.save()

            rss = rss_form.save()
            rss.user = user
            for feed in request.POST.getlist('subscribe'):
                rss.rss_feed.add(RssFeed.objects.get(feed_name=feed))
            rss.save()

            profile = UserProfile.objects.create(user=user)
            profile.save()

            return redirect('main:landing')
        else:
            return render(request, 'login/register.html',
                          {'user_form': user_form, 'rss_form': rss_form})

    def get(self, request):
        user_form = UserForm()
        rss_form = RssSubscribeForm()
        return render(request, 'login/register.html',
                      {'user_form': user_form, 'rss_form': rss_form})


class LogoutView(generic.View):

    @method_decorator(decorators.login_required)
    def get(self, request):
        logout(request)
        return redirect('main:landing')


class UserView(generic.View):

    @method_decorator(decorators.login_required)
    def get(self, request):
        return render(request, 'home.html')
