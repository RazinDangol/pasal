from django.shortcuts import render , render_to_response

# Create your views here.
from .models import Product,Category

def show(request):
    products=Product.objects.all()
    return render_to_response('products.html',{'products':products})

def cart():
	pass