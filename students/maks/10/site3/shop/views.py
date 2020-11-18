from django.shortcuts import render
from shop.models import Page

# Create your views here.

def index(request):
    page = Page.objects.all()
    return render(request,'index.html',{"page": page})