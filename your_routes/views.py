from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from trains.models import passangers_routes
# Create your views here.

def your_routes(request):
    if User.is_authenticated:
        passangers_routes_objects = passangers_routes.objects.filter(users = request.user)
        return render(request,"your_routes.html",{'passangers_routes_objects':passangers_routes_objects})

def cancel_route(request):
    if request.method == 'POST':
        id = request.POST['routep_id']
        cancelroute= passangers_routes.objects.get(id=id)
        cancelroute.delete()
    return redirect("/your_routes")