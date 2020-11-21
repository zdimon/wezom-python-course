from django.shortcuts import render
from page.models import Page

def index(request):
    pages = Page.objects.all()
    
    return render(request,'index.html',{"pages": pages})
