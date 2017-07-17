from django.contrib import admin

# Register your models here.
from .models import Temperature, Humidity, Rain

admin.site.register(Temperature)
admin.site.register(Humidity)
admin.site.register(Rain)