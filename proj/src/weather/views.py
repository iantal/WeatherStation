from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Temperature, Humidity, Rain
# Create your views here.

#function based view
def home(request):
	some_list = [5,2,3,454]
	context = {
		"bool_item" : True,
		"num" : 1234,
		"some_list" : some_list,
	}
	return render(request, "home.html", context)

def about(request):
	some_list = [5,612,3,4]
	context = {
	}
	return render(request, "about.html", context)

def contact(request):
	some_list = [5,2,3,443]
	context = {}
	return render(request, "contact.html", context)

def temp_hum(request):
	context = {}
	return render(request, "temp_hum.html",context)

def rain(request):
	context = {}
	return render(request, "rain.html",context)


class ContactView(View):
	def get(delf, request, *args, **kwargs):
		context = {}
		return render(request, "contact.html", context)



#ChartJS

class ChartHomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'rain.html',{})

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Satuday", "Sunday"]
        default_items = [2.1, 2.2, 2, 3, 4, 2,1.5]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


def get_data(request, *args, **kwargs):
	data = {
	'user':'miki',
	'sal':1000
	}
	return JsonResponse(data)

# Models for data
# def temps(request):
	
# 	template_name = 'restaurants/temperatures.html'
# 	queryset = Temperature.objects.all()
# 	context = {
# 		"object_list": queryset

# 	}
# 	return render(request, template_name, context)

# def hums(request):
	
# 	template_name = 'restaurants/humidities.html'
# 	queryset = Humidity.objects.all()
# 	context = {
# 		"object_list": queryset

# 	}
# 	return render(request, template_name, context)


# def rains(request):
	
# 	template_name = 'restaurants/rains.html'
# 	queryset = Rain.objects.all()
# 	context = {
# 		"object_list": queryset

# 	}
# 	return render(request, template_name, context)