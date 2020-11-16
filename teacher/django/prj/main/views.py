from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
    return render(req,'index.html',{'name': 'Dima'})

def about(req):
    return render(req,'about.html',{'name': 'Dima'})

def contact(req):
    return render(req,'contact.html',{'name': 'Dima'})
