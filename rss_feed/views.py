from django.shortcuts import render
from django.views import generic

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
	def get(self,request):
		return render(request, 'login/register.html')
