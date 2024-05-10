
from django.shortcuts import render
from django.http import HttpResponse


def firstview(request):
    message = '<h1> Hello Alex! </h1>'
    return HttpResponse(message)




# Create your views here.
