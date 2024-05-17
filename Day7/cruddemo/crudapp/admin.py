from django.contrib import admin
from crudapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list=['stud_no','stud_name','stud_class','stud_address','stud_gender']

admin.site.register(Student,StudentAdmin)