from django import forms

# Register Forms models here.

class EmployeeInfoForm(forms.Form):
    name = forms.CharField()
    salary= forms.IntegerField()
