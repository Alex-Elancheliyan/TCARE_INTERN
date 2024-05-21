from django.shortcuts import render
from crudapp.models import Student
from crudapp.forms import StudentForms
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

def read_students(request):
    students =  Student.objects.all()
    return render(request,'crudapptemp/index.html',{'students':students})

def create_view(request):
    form = StudentForms()
    if request.method == 'POST':
       form =StudentForms(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/check')
   
    return render(request, 'crudapptemp/create.html',{'form':form})

def delete_view(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/check')
    return render(request, 'crudapptemp/delete.html', {'student': student})

def update_view(request,id ):
    student = Student.objects.get(id=id)
    #form = StudentForms(instance=student)
    if request.method == 'POST':
        form = StudentForms(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'crudapptemp/update.html', {'student': student})
