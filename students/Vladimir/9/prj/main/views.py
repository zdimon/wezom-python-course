from django.shortcuts import render
from main.models import Page

def index(request):
    return render(request, 'index.html')

def index(request):
    page = Page.objects.get(id=7)
    return render(request, 'index.html', {"page": page})
