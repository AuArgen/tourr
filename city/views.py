from django.shortcuts import render, redirect

from city.models import City, About
from gallery.models import Gallery
from post.models import Post, Order


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


def about(request):
    about = About.objects.first()
    context = {
        'about': about,
    }
    return render(request, 'about.html', context)


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def orderSave(request, pk):
    if request.method == 'POST':
        name = request.POST['name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        comment = request.POST['comment']
        post = Post.objects.get(id=pk)
        if not post:
            return redirect('/')
        Order.objects.create(post=post,name=name, last_name=last_name, email=email, phone=phone, comment=comment)
        return redirect('/success')
    return redirect('/')

def success(request):
    return render(request, 'success.html')