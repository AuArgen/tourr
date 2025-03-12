from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('city/<int:pk>', showCity, name='show_city'),
    path('post/<int:pk>', showPost, name='show_post'),

    path('cities', cities, name='cities'),
]