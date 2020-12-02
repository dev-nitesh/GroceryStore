from django.shortcuts import render, HttpResponse
import math, random
# Create your views here.
from .models import StoreOTPVerificationLinks
from user_handler.models import USERS
def generateOTP():
    string = '0123456789'
    OTP = ''
    length = len(string)
    for i in range(6):
        OTP += string[math.floor(random.random() * length)] 
    return OTP
genrated_otp = generateOTP()


def send_verification_link(user):
    
    StoreOTPVerificationLinks(OTP=genrated_otp,mobileNo=user.phone,uid=user.id).save()
    return genrated_otp

def validate_otp(request):
   if request.method == 'POST':
        OTP=request.POST['otp']
        
        sm=StoreOTPVerificationLinks.objects.filter(OTP=OTP).values('id')
        #uid=sm.uid         
        print (sm)
        
        if not sm:
            return HttpResponse('OTP Validation failed')
        fetchid= sm[0]['id']
        user=USERS.objects.get(id=fetchid)
        user.otp_validate=1
        user.save()
        #for s in sm:
        #   s.delete()
        return HttpResponse('Your phone number validated Successfully')
        
    
   return render(request, 'signup.html')


