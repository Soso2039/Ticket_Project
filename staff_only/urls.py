from django.urls import path
from . import views


urlpatterns = [
    path('', views.staff_only, name="staff_only"),
    path('add_station', views.add_station, name="add_station"),
    path('addrecord_station',views.addrecord_station, name="addrecord_station"),
    path('add_route', views.add_route, name="add_route"),
    path('addrecord_route', views.addrecord_route, name="addrecord_route"),
    path('deleteroute', views.deleteroute, name='deleteroute'),
    path('deletestation', views.deletestation, name='deletestation'),
]