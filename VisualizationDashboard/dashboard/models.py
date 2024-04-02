from django.db import models

class Incident(models.Model):
    intensity = models.CharField(max_length=100)
    likelihood = models.CharField(max_length=100)
    relevance = models.CharField(max_length=100)
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    topics = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
