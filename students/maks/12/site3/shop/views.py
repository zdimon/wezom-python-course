from django.shortcuts import render
from shop.models import Page
from shop.models import Product
from shop.models import Category
from shop.models import Busket
from easy_thumbnails.files import get_thumbnailer
# Create your views here.

def index(request):
    pages = Page.objects.all()
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request,'index.html',{"pages": pages, "product": product, "category": category})

def busket_data(request):
    product = Product.objects.all()
    return render(request,'index.html',{"product": product})

def doregistration(request):
	if request.method == "POST":
		user = User()
		user.save
		print("This is post")
		print(request.POST("login"))
		print(request.POST("password"))
	return render(request,'registration_success.html',{"product": product})