from django.shortcuts import render
from page.models import Page, Catalog, Product, Basket
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import *
from .forms import ProductForm

def index(request):
    pages = Page.objects.all()
    catalogs = Catalog.objects.all()
    products = Product.objects.all()

    return render(request,'index.html', \
    { \
        "pages": pages, \
        "catalogs": catalogs, \
        "products": products, \
        "form": ProductForm()
    })


def product(request,id):
    print(id)
    product = Product.objects.get(pk=id)
    return render(request,'product.html', {"product": product})

def saveorder(request):
    product = Product.objects.get(pk=request.POST['product_id'])
    b = Basket()
    b.name = request.POST['username']
    b.phone = request.POST['phone']
    b.product = product
    b.save()
    # print(request.POST['product_id'])
    return render(request,'product.html', {"product": product})


def doregistration(request):
    if request.method == 'POST':
        user = User()
        user.username = request.POST['login']
        user.set_password(request.POST['password'])
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()
        print('This is post')
        print(request.POST['login'])
        print(request.POST['password'])
    return render(request,'register_success.html')

def dologin(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['login'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            print('Wrong user')