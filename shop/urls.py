from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hello'),
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
]