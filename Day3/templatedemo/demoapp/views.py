from django.shortcuts import render
import datetime

# Create your views here.
def display(request):
    message = " Hello "
    name = " TCARE, "
    timenow = datetime.datetime.now()
    hours = int(timenow.strftime("%H"))
    if hours <12 :
        message += name + "Good Morning!"

    else: 
        message+="Good Evening" +name
    details = {"display_time": timenow,"message":message, "name":name }
    

    return render(request,'demoapptemp/blog.html',context = details)
