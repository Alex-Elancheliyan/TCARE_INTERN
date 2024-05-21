from django import forms
from crudapp.models import Student

class StudentForms(forms.ModelForm):
    class Meta:                        #metadata is DATA about DATA.
        model = Student               #Student - Class of models.py.
        fields = '__all__'             #fields of model class Student.


