from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# Create your views here.
from .models import Product, Category, Customer, Sales, Review
from .forms import Signup
categories = Category.objects.all()

parent=Category.objects.filter(parent=None)
categories=Category.objects.exclude(parent = None)

form=Signup() 

def show(request):
    products = Product.objects.all()
    
    return render(request,'products.html', {'products': products,'categories':categories,'parent':parent,'form':form})


def category(request):
	
	return render(request,'categories.html', {'categories': categories,'parent':parent,'form':form})


def customer(request):
	
    customers = Customer.objects.all()
    return render(request,'customer.html', {'customers': customers,'categories':categories,'parent':parent,'form':form})


def sales(request):
    sales = Sales.objects.all()
    return render(request,'sales.html', {'sales': sales,'categories':categories,'parent':parent,'form':form})

def product_id(request,id):
	product=Product.objects.get(id=id)
	reviews= Review.objects.filter(product_id=id)
	print(reviews)
	return render(request,'product.html',{'product':product,'reviews':reviews,'categories':categories,'parent':parent,'form':form})

def signup(request):
	 
	print(request.POST)
	if request.method == 'POST':
		form=Signup(request.POST)
		print(form)
		if form.is_valid():
			new_join=form.save(commit=False)
			full_name=form.cleaned_data['full_name']
			address=form.cleaned_data['address']
			mobile=form.cleaned_data['mobile']
			email=form.cleaned_data['email']
			password=form.cleaned_data['password']
			new_join,created=Customer.objects.get_or_create(full_name=full_name,address=address,mobile=mobile, email=email,password=password)			
			print(new_join, created)
			return HttpResponse('success')
	else:
		form=Signup()
	return render(request,'signup.html',{'form':form})

