from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from trains.models import route, station
from django import forms
# Create your views here.


def staff_only(request):
    stations = station.objects.all()
    routes = route.objects.all()
    return render(request, "staff_only/template/staff_only.html",{
    "stations":stations,
    "routes":routes,
    })

def add_station(request):
    return render(request, "staff_only/template/add_station.html")

def addrecord_station(request):
    if request.method == "POST":
        a = request.POST['city']
        b = request.POST['station']
        c = request.POST['longitude']
        d = request.POST['latitude']
        x = station(city=a, station=b, longitude=c, latitude=d)
        x.save()
    return render(request, "staff_only/template/add_station.html",{
        "message": "Station added"
        })

def add_route(request):
    return render(request, "staff_only/template/add_route.html",{
        "stations":station.objects.all()
    })

class routeform(forms.Form):
    origin = forms.ModelChoiceField(queryset=station.objects.all())
    destination = forms.ModelChoiceField(queryset=station.objects.all())
    duration = forms.IntegerField()
    cost = forms.IntegerField()
    class Meta:
        model = route
        fields = ['origin', 'destination', 'duration', 'cost']


def addrecord_route(request):
    if request.method == 'POST':
        form = routeform(request.POST)
        if form.is_valid():
            origin_pk = form.cleaned_data['origin']
            a = station.objects.get(station=origin_pk)
            destination_pk = form.cleaned_data['destination']
            b = station.objects.get(station=destination_pk)
            c = form.cleaned_data['duration']
            d = form.cleaned_data['cost']
            route_append = route(origin=a, destination=b, duration=c, cost=d)
            route_append.save()
            return render(request,'staff_only/template/add_route.html',{
                "stations":station.objects.all(),
                "message": "Route added!"
            })
        else:
            form = routeform()
    return render(request, 'add_route.html', {'form': form})

def deleteroute(request):
    if request.method == 'POST':
        id = request.POST['route_id']
        deleteroute= route.objects.get(id=id)
        deleteroute.delete()
        return redirect("/staff_only")

def deletestation(request):
    if request.method == 'POST':
        id = request.POST['station_id']
        deletestation= station.objects.get(id=id)
        deletestation.delete()
        return redirect("/staff_only")