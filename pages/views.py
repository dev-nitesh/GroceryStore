from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from user_handler.models import USERS

def index(request):
    return render(request, 'index.html')


def output(request):
    return render(request, 'login.html')


def user_details(request , id):
    user_details = get_object_or_404(USERS, pk=id)    
    context = {
      'user_details': user_details
    }
    return render(request, 'user_details.html' , context)