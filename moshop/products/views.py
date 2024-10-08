from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    print("Index view is called")  # This will print when the view is called
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def new(request):
    return HttpResponse('New Products')
