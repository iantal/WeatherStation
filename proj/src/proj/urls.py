
from django.conf.urls import url
from django.contrib import admin

from weather.views import home,about, contact,temp_hum,rain
from weather.views import ContactView, ChartHomeView, ChartData, THData, THHomeView

#static stuff
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^about/$', about),
    url(r'^contact/$', ContactView.as_view()),
    url(r'^temp_hum/$', temp_hum),
    url(r'^rain/$', ChartHomeView.as_view()),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^temperature/$', THHomeView.as_view()),
    url(r'^api/temperature/data/$', THData.as_view()),    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)