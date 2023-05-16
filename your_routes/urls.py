from django.urls import path
from . import views

urlpatterns = [
    path('', views.your_routes, name='your_rotues'),
    path('cancel_route',views.cancel_route, name='cancel_route')
]