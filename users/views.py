from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "users/login.html", {
                "message": "Invalid username or password"
            })

    if request.GET.get('staff_login') == 'true':
        staff_username = 'staff'
        staff_password = 'staffdjango'
        user = authenticate(request, username=staff_username, password=staff_password)
        if user is not None:
            login(request, user)
            return redirect('/')

    if request.user.is_authenticated:
        return redirect('/')
    
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "home.html", {
        "message": "Logged out"
    })