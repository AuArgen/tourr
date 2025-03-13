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


def cities(request):
    cities = City.objects.all().order_by('id')
    context = {
        'cities': cities,
    }
    return render(request, 'cities.html', context)


def posts(request):
    posts = Post.objects.all().order_by('id')
    context = {
        'posts': posts,
    }
    return render(request, 'posts.html', context)


def galleries(request):
    galleries = Gallery.objects.all().order_by('id')
    data = [galleries[i:i + 6] for i in range(0, len(galleries), 6)]
    context = {
        'galleries': data,
    }
    return render(request, 'gallery.html', context)
