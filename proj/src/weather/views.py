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

def temperature(request):
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


class TemperatureView(View):
	def get(delf, request, *args, **kwargs):
		context = {}
		return render(request, "temperature.html", context)


class HumidityView(View):
	def get(delf, request, *args, **kwargs):
		context = {}
		return render(request, "humidity.html", context)



#ChartJS

class RainYearData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, year, format=None):
        labels = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        default_items = list(Rain.objects.values('date', 'value').filter(date__startswith=year));
        data = {
        	"labels" : labels,
            "default": default_items,
        }
        return Response(data)


class TempData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, sy, sm, sd, ey, em, ed, format=None):
    	start_date = sy + "-" +sm + "-" + sd;
    	end_date = ey + "-" +em + "-" + ed;
    	print("S: " + start_date)
    	print("E: " + end_date)
        response = JsonResponse(dict(
        	temps = list(Temperature.objects.values('date', 'value').filter(
        		date__gte=start_date, date__lte=end_date))))
        	# temps = list(Temperature.objects.values('date', 'value').filter(date__gte='2017-07-06T00:00:00Z', date__lte='2017-07-06T15:00:00Z'))))
        return response


class HumidityData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, sy, sm, sd, ey, em, ed, format=None):
    	start_date = sy + "-" +sm + "-" + sd;
    	end_date = ey + "-" +em + "-" + ed;
    	print("S: " + start_date)
    	print("E: " + end_date)
        response = JsonResponse(dict(
        	temps = list(Humidity.objects.values('date', 'value').filter(
        		date__gte=start_date, date__lte=end_date))))
        	
        return response


class ChartHomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'rain.html',{})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        default_items = list(Rain.objects.values('date', 'value'));
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
        	# temps=list(Temperature.objects.values('date', 'value'))))
        	temps = list(Temperature.objects.values('date', 'value'))))
        	# temps = list(Temperature.objects.values('date', 'value').filter(date__gte='2017-07-06T00:00:00Z', date__lte='2017-07-06T15:00:00Z'))))
        return response

