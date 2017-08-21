
from django.conf.urls import url
from django.contrib import admin

from weather.views import home, contact,temp_hum,rain, RainYearData, TempData, HumidityData
from weather.views import ChartHomeView, ChartData, THData, TemperatureView, HumidityView

#static stuff
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^temperature/$', TemperatureView.as_view()),
    url(r'^humidity/$', HumidityView.as_view()),
    # url(r'^temp_hum/$', temp_hum),
    url(r'^rain/$', ChartHomeView.as_view()),
    # url(r'^temperature/$', THHomeView.as_view()),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^api/rain/(?P<year>\d{4})/$', RainYearData.as_view()),
    url(r'^api/temp/(?P<sy>\d{4})/(?P<sm>\d{2})/(?P<sd>\d{2})/(?P<ey>\d{4})/(?P<em>\d{2})/(?P<ed>\d{2})/$', TempData.as_view()),
    url(r'^api/hum/(?P<sy>\d{4})/(?P<sm>\d{2})/(?P<sd>\d{2})/(?P<ey>\d{4})/(?P<em>\d{2})/(?P<ed>\d{2})/$', HumidityData.as_view()),
      
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)