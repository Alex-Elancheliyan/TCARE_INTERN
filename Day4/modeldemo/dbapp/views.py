from django.shortcuts import render
from dbapp.models import Student

def stud_details(request):

    data = Student.objects.all()
    stud_dict={'stud_list':data}

    return render(request,"dbapptemplates/blog.html",context=stud_dict)
