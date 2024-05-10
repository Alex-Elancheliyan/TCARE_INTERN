
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def gm(request):
    message = "<h1> Good Morning World"
    return HttpResponse(message)

def ga(request):
    message = "<h1> Good Afternoon World"
    return HttpResponse(message)

def gn(request):
    message = "<h1> Good Night World"
    return HttpResponse(message)

def timenow(request):
    dt= datetime.datetime.now()
    time = dt.strftime('%H:%M:%S')  
    result = '<h1> The System Time is: '+ str(time)+ '</h1>'
    return HttpResponse(result)



# Create your views here.
