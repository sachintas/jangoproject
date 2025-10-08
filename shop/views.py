from django.shortcuts import render
from .models import Product
# Create your views here.
def home(request):
    latest_products = Product.objects.order_by('-created_at')[:2]
    context = {"name": "Sachin","products":latest_products}
    return render(request, 'index.html', context)
def shop(request):
    products = Product.objects.order_by('created_at')
    context = {'title':'shop',"products": products}
    return render(request, 'shop/products_list.html', context)
def singleProduct(request, pk):
    product = Product.objects.get(pk = pk)
    context = {'title':product.name,"product": product}
    return render(request, 'shop/single-product.html', context)