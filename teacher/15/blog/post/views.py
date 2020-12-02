from django.shortcuts import render
from .models import Post
# Create your views here.
from django.core.paginator import Paginator

def blog(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 15)
    page_number = request.GET.get('page',1)
    posts = paginator.get_page(page_number)
    return render(request,'blog_list.html', {'posts': posts})
