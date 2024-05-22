from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

class FirstView(View):
    def get(self,request):
        return HttpResponse('<h1> Hello </h1>')
    
class SecondView(TemplateView):
    template_name = 'cbvapptemp/blog.html'
    




