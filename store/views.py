from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'home.html')

def rental(request):
    products = Product.objects.filter(category='rental')
    return render(request, 'rental.html', {'products': products})

def surgical(request):
    products = Product.objects.filter(category='surgical')
    return render(request, 'surgical.html', {'products': products})