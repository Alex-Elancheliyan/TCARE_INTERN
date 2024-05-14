from django.contrib import admin

from dbapp.models import Student

# Register your models here.


class Studentadmin(admin.ModelAdmin):
    stud_details= ['student_name','student_rollno','student_total']

admin.site.register(Student,Studentadmin)
