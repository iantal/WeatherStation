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