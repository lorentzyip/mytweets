from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Index(View):
	def get(self, request):
		params = {}
		params["name"] = "Django"
		return render(request, 'base.html', params)
		
class Profile(View):
	def get(self, request, username):
		params = dict()()()
		user = User.objects.get(username=username)
		tweets = Tweet.objects.filter(user=user)
		params["tweets"] = tweets
		params["user"] = user
		return render(request, 'profile.html', params)