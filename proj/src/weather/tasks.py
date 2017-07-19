# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .models import Temperature, Humidity

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

import requests
import json


def getTempAndHum(channel,api_key,results):
	url = 'https://api.thingspeak.com/channels/'+str(channel)+ \
		  	'/feeds.json?api_key='+str(api_key)+ \
			'&results='+str(results)
	resp = requests.get(url)
	data = json.loads(resp.text)
	list_of_data = []
	for i in range(results):
		created_at=str(data['feeds'][i]['created_at'])
		humidity = str(data['feeds'][i]['field2'])
		temperature = str(data['feeds'][i]['field1'])
		l = [created_at, humidity, temperature]
		list_of_data.append(l)
	return list_of_data

# print(getTempAndHum(channel=298116,api_key='K0S8YEA42QOGSV9D',results=2))
@shared_task
def insert_temp_and_hum():
	data = getTempAndHum(channel=298116,api_key='K0S8YEA42QOGSV9D',results=30)

	for item in data:
		try:
			Temperature.objects.create(date=item[0],value=item[2])
			Humidity.objects.create(date=item[0],value=item[1])
		except:
			pass