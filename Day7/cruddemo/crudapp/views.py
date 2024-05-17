from django.shortcuts import render
from crudapp.models import Student
# Create your views here.

def read_students(request):
    students =  Student.objects.all()

    return render(request,'crudapptemp/index.html',{'students':students})
