from django.contrib import admin

from .models import station, route, passangers_routes

# Register your models here.



admin.site.register(station)
admin.site.register(route)
admin.site.register(passangers_routes)
