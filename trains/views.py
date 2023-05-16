from django.shortcuts import render, redirect
from django.db.models import Q
from .models import route, station, passangers_routes
from django.contrib.auth.models import User
import random
from django.contrib import messages

# Create your views here.
def search (request):
    if request.method == 'POST':
        search_origin = request.POST['search_origin']
        search_destination = request.POST['search_destination']
        routes = route.objects.filter(Q(origin=search_origin), Q(destination=search_destination))
        stations_longitude1 = station.objects.filter(Q(id=search_origin)).values_list('longitude', flat=True)
        stations_latitude1 = station.objects.filter(Q(id=search_origin)).values_list('latitude', flat=True)
        stations_longitude2 = station.objects.filter(Q(id=search_destination)).values_list('longitude', flat=True)
        stations_latitude2 = station.objects.filter(Q(id=search_destination)).values_list('latitude', flat=True)
        return render (request, 'search.html',{'routes':routes,'stations_longitude1':stations_longitude1,'stations_latitude1':stations_latitude1,
        'stations_longitude2':stations_longitude2,'stations_latitude2':stations_latitude2})
    else:
        return render (request, 'home.html')

def search2 (request):
    if request.method == 'POST':
        route_id = request.POST['route_id']
        routes=route.objects.filter(id=route_id)
        obj1 = route.objects.get(id=route_id)
        stationid1 = obj1.origin_id
        stationid2 = obj1.destination_id
        stations_longitude1 = station.objects.filter(Q(id=stationid1)).values_list('longitude', flat=True)
        stations_latitude1 = station.objects.filter(Q(id=stationid1)).values_list('latitude', flat=True)
        stations_longitude2 = station.objects.filter(Q(id=stationid2)).values_list('longitude', flat=True)
        stations_latitude2 = station.objects.filter(Q(id=stationid2)).values_list('latitude', flat=True)
        return render (request, 'search.html',{
            'routes':routes,'stations_longitude1':stations_longitude1,'stations_latitude1':stations_latitude1,
        'stations_longitude2':stations_longitude2,'stations_latitude2':stations_latitude2
        })

def home (request):
    return render (request, 'trains.html', {
        "stations":station.objects.all()
    })

def home2 (request):
    x= route.objects.all()
    count = x.count()
    random_id = random.sample(range(count),5)
    random_routes = [x[i] for i in random_id]
    return render (request, 'home.html', {
        "route":random_routes,
    })


def buy(request):
    if request.method == "POST":
        x = request.POST["route_id"]
        y = User.objects.get(id = request.user.id)
        x = route.objects.get(id=x)
        z = passangers_routes(users = y, route = x)
        z.save()
        messages.success(request, "Ticket bought")
        return redirect("/")

