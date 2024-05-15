from django.shortcuts import render
from formsapp.forms import EmployeeInfoForm
# Create your views here.

def empDetailsView(request):
    form =EmployeeInfoForm()
    empInfo= {'form':form}
    return render(request,"formsapptemp/input.html",context=empInfo)



