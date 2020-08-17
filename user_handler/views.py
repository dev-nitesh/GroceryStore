from django.shortcuts import render,HttpResponse,redirect
from .models import USERS
from custom_services.models import StoreOTPVerificationLinks
from custom_services.views import send_verification_link
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username=request.POST['Username']
        email=request.POST['Email']
        password=request.POST['Password']
        phone=request.POST['Phone']
        user = USERS(email=email,user=username,
        password=password,phone=phone)
        user.save()
        otp=send_verification_link(user)
        return HttpResponse ('Your OPT for signup is \n'+ otp )
        #return render(request, 'validate.html')
    return render(request, 'signup.html')
