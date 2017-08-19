from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Temperature, Humidity, Rain

from django.forms.models import model_to_dict
from django.core import serializers
import json
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


def time(request):
	context = {}
	return render(request, "time.html",context)

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

class THHomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'th.html',{})

class THData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        response = JsonResponse(dict(
        	temps=list(Temperature.objects.values('date', 'value'))))
        return response

