from django.shortcuts import render
from . import forms

def index(request):
    return render(request,'testapp/index.html')

def form_name_view(request):
    form = forms.FormName()
    return render(request,'testapp/form_page.html',{'form':form})
