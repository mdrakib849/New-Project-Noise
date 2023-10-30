from django.shortcuts import render
from django.http import HttpResponse
from nHome.models import Post, Category


# Create your views here.
def homepage(request):
    # load all the post form db (10)
    post = Post.objects.all()[:11]

    cats = Category.objects.all()
    data = {
        'posts': post,
        'cats': cats
    }

    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    return render(request, 'posts.html', {'post': post, 'cats': cats})


def catagory(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, 'catagory.html', {'cat':cat, 'posts':posts})



def aboutpage(request):
    return render(request,'aboutpage.html')
