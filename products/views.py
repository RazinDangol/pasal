from django.shortcuts import render , render_to_response

# Create your views here.
from .models import Product

def show(request):
    products=Product.objects.all()
    print(products)
    return render_to_response('show.html',{'products':products})
