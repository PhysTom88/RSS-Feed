from django.shortcuts import redirect, render
from django.views import generic

from .forms import UserForm, RssSubscribeForm
from .models import UserProfile


class HomeView(generic.View):
    '''View for home page

       Displays current list of rss with option to
       favourite a selection
    '''

    def get(self, request):
        return render(request, 'home.html')


class LoginView(generic.View):
    def get(self, request):
        return render(request, 'login/login.html')


class RegisterView(generic.View):

    def post(self, request):
        user_form = UserForm(request.POST)
        rss_form = RssSubscribeForm(request.POST)
        if user_form.is_valid() and rss_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.username = user.email
            user.save()

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
