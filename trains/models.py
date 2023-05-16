from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class station(models.Model):
    city = models.CharField(max_length=64)
    station = models.CharField(max_length=64)
    longitude = models.FloatField(default=1)
    latitude = models.FloatField(default=1)
    def __str__(self):
        return f"{self.station}"


class route(models.Model):
    origin = models.ForeignKey(station, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(station, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    cost = models.IntegerField()
    def __str__(self):
        return f"from: {self.origin} to {self.destination}. "

class passangers(models.Model):
    users = models.ManyToManyField(User, blank=True, related_name="users")
    route = models.ManyToManyField(route, blank=True, related_name="passengers")
    def __str__(self):
        return f'{self.users}'

class passangers_routes(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    route = models.ForeignKey(route, on_delete=models.CASCADE, related_name="route")
    def __str__(self):
        return f'{self.users}'
