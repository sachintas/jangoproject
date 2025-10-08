from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='welcome'),
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shop/<int:pk>/', views.singleProduct, name='singleProduct'),
]