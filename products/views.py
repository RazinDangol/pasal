from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
# Create your views here.
from .models import Product, Category, Customer, Sales, Review
from .forms import Signup, Login

from django.contrib.auth.models import User
categories = Category.objects.all()


parent = Category.objects.filter(parent=None)
categories = Category.objects.exclude(parent=None)

form = Signup()
login_form = Login()


def show(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products, 'categories': categories, 'parent': parent, 'form': form, 'login': login_form})


def category(request):
    return render(request, 'categories.html', {'categories': categories, 'parent': parent, 'form': form})


def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers, 'categories': categories, 'parent': parent, 'form': form})


def sales(request):
    sales = Sales.objects.all()
    return render(request, 'sales.html', {'sales': sales, 'categories': categories, 'parent': parent, 'form': form})


def product_id(request, id):
    product = Product.objects.get(id=id)
    reviews = Review.objects.filter(product_id=id)
    print(reviews)
    return render(request, 'product.html', {'product': product, 'reviews': reviews, 'categories': categories, 'parent': parent, 'form': form})


def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/signup/success/')
    else:
        form = Signup()
    return render(request, 'signup.html', {'form': form})


def signup_success(request):
    return HttpResponse('Successfully created account')


def login(request):
    if request.method == 'POST':
        login_form = Login(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect('/login/success')
                else:
                    return HttpResponseRedirect('/login/disabled')
            else:
                return HttpResponseRedirect('/login/invalid')
    else:
        login_form = Login()
        return render(request, 'login.html', {'form': login_form})


def login_success(request):
    return HttpResponse('Successfully logged in')


def login_invalid(request):
    return HttpResponse('Wrong username of password')


def login_disabled(request):
    return HttpResponse('Sorry but your account is disabled')
