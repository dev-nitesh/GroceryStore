from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import USERS
from custom_services.models import StoreOTPVerificationLinks
from custom_services.views import send_verification_link
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username=request.POST['Username']
        email=request.POST['Email']
        password=request.POST['Password']
        phone=request.POST['Phone']
        if USERS.objects.filter(user=username).exists():
            messages.warning(request,'Username already taken')
            return redirect('/')
        elif USERS.objects.filter(email=email).exists():
            messages.warning(request,'This email is already registered with us')
            return redirect('/')
        else:

            user = USERS(email=email,user=username,
            password=password,phone=phone)
            user.save()
            otp=send_verification_link(user)
#            return HttpResponse ('Your OPT for signup is \n'+ otp )
            return render(request, 'validate.html')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        Password=request.POST['Password']
    
        us=USERS.objects.filter(user=Username).values('user','password','otp_validate','id')
        if not us:
            return HttpResponse('User does not exists')
        fetch_otp_validate=us[0]['otp_validate']
        fetch_user=us[0]['user']
        fetch_pwd= us[0]['password']
        fetch_id=us[0]['id']
        if fetch_otp_validate == 0:
            return HttpResponse('User does not exists')
        if fetch_user == Username and fetch_pwd == Password :
            userLogin=get_object_or_404(USERS, pk=fetch_id)
            context = {
            'userLogin': userLogin
             }
            return render(request, 'home.html' , context)
            #return abc()
        else :
            return HttpResponse('Invalid Credentials')


