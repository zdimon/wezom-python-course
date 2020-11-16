from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(req, 'index.html', {'name': 'Vladimir'})

def about(req):
    return render(req, 'about.html',{'name': 'Vladimir'})

def shortcodes(req):
    return render(req, 'shortcodes.html',{'name': 'Vladimir'})
