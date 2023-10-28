from django.shortcuts import render
from django.http import HttpResponse
from nHome.models import Post


# Create your views here.
def homepage(request):
    # load all the post form db (10)
    post = Post.objects.all()[:11]
    data = {
        'posts': post
    }

    return render(request, 'home.html', data)
