from django.shortcuts import render
import string
import random

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import*
# Create your views here.


def getfeedback(request):
    return render(request,'feedback.html')

def feedbackloginfunction(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')

        comment=request.POST.get('comment')


        tosend=comment + '---------------This was your Feedback'+'\n' +'Thank You for Your Feedback'


        Feedback.objects.create(name=name,email=email,comment=comment)



    send_mail(
        'Thank you for contacting us',
        tosend,
        'likhkhel73@gmail.com',
        [email],
        fail_silently=False,
    )

    return redirect('blogs')

    return render(request, 'error.html')


#----------------------------------------------#
#----------------------------------------------#
#----------------------------------------------#
#----------------------------------------------#
#----------------------------------------------#










