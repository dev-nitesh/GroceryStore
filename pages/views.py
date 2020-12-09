from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from user_handler.models import USERS
from products.models import Category

def index(request):
    products=Category.objects.all()

    context = {
        'products': products,
        
    }
    #render(request, 'partials/sidebar.html' , context)
    return render(request, 'index.html' , context)


def output(request):
    return render(request, 'login.html')


def user_details(request , id):
    user_details = get_object_or_404(USERS, pk=id)    
    context = {
      'user_details': user_details
    }
    return render(request, 'user_details.html' , context)


def products(request , id):
    products = get_object_or_404(Category, pk=id)    
    context = {
      'products': products
    }
    url=products.name
    return render(request, 'products/products.html' , context)
