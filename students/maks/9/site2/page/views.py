from django.shortcuts import render
from page.models import Page

# Create your views here.

def index(request):
    pages = Page.objects.all()
    return render(request,'index.html',{"pages": pages})
