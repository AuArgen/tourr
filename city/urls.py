from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('city/<int:pk>', showCity, name='show_city'),
    path('post/<int:pk>', showPost, name='show_post'),

    path('cities', cities, name='cities'),
    path('posts', posts, name='posts'),
    path('galleries', galleries, name='galleries'),
    path('about', about, name='about'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('success', success, name='success'),
    path('order_save/<int:pk>', orderSave, name='order_save'),
]