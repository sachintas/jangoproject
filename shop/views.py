from django.shortcuts import render
from .models import Product
# Create your views here.
def home(request):
    context = {"name": "Sachin"}
    return render(request, 'index.html', context)
def shop(request):
    products = Product.objects.all()
    context = {'title':'shop',"products": products}
    return render(request, 'shop.html', context)