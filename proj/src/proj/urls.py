"""muypicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from weather.views import home,get_data,about, contact,temp_hum,rain
from weather.views import ContactView, ChartHomeView, ChartData
from weather.views import temps,hums,rains

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^about/$', about),
    url(r'^contact/$', ContactView.as_view()),
    url(r'^temp_hum/$', temp_hum),
    url(r'^rain/$', ChartHomeView.as_view()),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    
    url(r'^temps-api/$', temps),
    url(r'^hums-api/$', hums),
    url(r'^rains-api/$', rains),

]
