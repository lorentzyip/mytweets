from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Index(View):
	def get(self, request):
		params = {}
		params["name"] = "Django"
		return render(request, 'base.html', params)
		