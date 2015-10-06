from django.shortcuts import render, render_to_response

# Create your views here.
from .models import Product, Category, Customer, Sales


def show(request):
    products = Product.objects.all()
    return render_to_response('products.html', {'products': products})


def category(request):
    categories = Category.objects.all()
    for category in categories:
    	cat=category.parent
    	print(cat)
    return render_to_response('categories.html', {'categories': categories})


def customer(request):
    customers = Customer.objects.all()
    return render_to_response('customer.html', {'customers': customers})


def sales(request):
    sales = Sales.objects.all()
    return render_to_response('sales.html', {'sales': sales})
