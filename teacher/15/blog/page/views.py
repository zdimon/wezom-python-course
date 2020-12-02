from django.shortcuts import render

from page.models import Page

def index(request):
    page = Page.objects.get(id=1)
    return render(request,'index.html', {'page': page})


def page_detail(request,pagename):
    page = Page.objects.get(alias=pagename)
    return render(request,'index.html', {'page': page})