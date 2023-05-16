from django.urls import path
from . import views

urlpatterns = [
    path('search',views.search, name='search'),
    path('search2',views.search2, name='search2'),
    path('trains', views.home, name='trains'),
    path('', views.home2, name='home'),
    path('buy', views.buy, name='buy' ),
]