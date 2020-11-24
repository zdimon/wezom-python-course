from django.shortcuts import render
from page.models import Page, Catalog, Product, Basket

def index(request):
    pages = Page.objects.all()
    catalogs = Catalog.objects.all()
    products = Product.objects.all()

    return render(request,'index.html', \
    { \
        "pages": pages, \
        "catalogs": catalogs, \
        "products": products, \
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