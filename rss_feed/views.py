from django.contrib.auth import authenticate, login, logout, decorators
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import generic

from .forms import UserForm, RssSubscribeForm
from .models import UserProfile, RssFeed
from .rss_feed import get_rss_feeds


class HomeView(generic.View):
    '''View for home page

       Displays current list of rss with option to
       favourite a selection
    '''

    def get(self, request):
        if request.user.is_authenticated:
            feeds = get_rss_feeds()
        else:
            pass
        return render(request, 'home.html', {'feeds': feeds})


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
                          {'user_form': user_form})

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
