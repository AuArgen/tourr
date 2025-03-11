from django.shortcuts import render

from city.models import City


# Create your views here.
def home(request):
    cities = City.objects.filter(is_show=True).order_by('id')
    context = {
        'cities': cities
    }
    return render(request, 'index.html', context)