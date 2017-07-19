from django.db import models

# Create your models here.

class Temperature(models.Model):
	date = models.CharField(max_length=120, unique=True)
	value = models.FloatField(null=True)

	def __str__(self):
		return '{'+self.date+' : ' + str(self.value)+'}'


class Humidity(models.Model):
	date = models.CharField(max_length=120, unique=True)
	value = models.FloatField(null=True)

	def __str__(self):
		return '{'+self.date+' : ' + str(self.value)+'}'

class Rain(models.Model):
	date = models.CharField(max_length=120, unique=True)
	value = models.FloatField(null=True)

	def __str__(self):
		return '{'+self.date+' : ' + str(self.value)+'}'