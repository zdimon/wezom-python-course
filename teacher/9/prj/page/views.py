from django.shortcuts import render
from page.models import Page

def index(request):
    page = Page.objects.get(id=7)
    return render(request,'index.html',{"page": page})
