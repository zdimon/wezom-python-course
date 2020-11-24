from django.shortcuts import render
from shop.models import Page
from shop.models import Product
from shop.models import Category
from shop.models import Busket
# Create your views here.

def index(request):
    pages = Page.objects.all()
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request,'index.html',{"pages": pages, "product": product, "category": category})

def busket_data(request):
    return render(request,'index.html',{"": fname})