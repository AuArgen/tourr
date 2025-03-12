from django.shortcuts import render

from city.models import City
from gallery.models import Gallery
from post.models import Post


# Create your views here.
def home(request):
    cities = City.objects.filter(is_show=True).order_by('id')
    posts = Post.objects.filter(is_popular=True).order_by('id')
    galleries = Gallery.objects.filter(is_show=True).order_by('id')
    trend_posts = Post.objects.filter(is_trending=True).order_by('id')
    context = {
        'cities': cities,
        'posts': posts,
        'galleries': galleries,
        'trend_posts': trend_posts,
    }
    return render(request, 'index.html', context)

def showCity(request, pk):
    city = City.objects.filter(id=pk).first()
    posts = Post.objects.filter(city=city).order_by('id')
    galleries = Gallery.objects.filter(is_show=True).order_by('id')
    trend_posts = Post.objects.filter(is_trending=True).order_by('id')
    context = {
        'city': city,
        'posts': posts,
        'galleries': galleries,
        'trend_posts': trend_posts,
    }
    return render(request, 'show_city.html', context)

def showPost(request, pk):
    post = Post.objects.filter(id=pk).first()
    posts = Post.objects.filter(is_popular=True).order_by('id')
    galleries = Gallery.objects.filter(is_show=True).order_by('id')
    trend_posts = Post.objects.filter(is_trending=True).order_by('id')
    context = {
        'post': post,
        'posts': posts,
        'galleries': galleries,
        'trend_posts': trend_posts,
    }
    return render(request, 'show_post.html', context)