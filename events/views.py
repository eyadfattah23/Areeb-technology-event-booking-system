from django.shortcuts import render
from django.http import HttpResponse

from .models import Event
# Create your views here.


def home(request):
    query_set = Event.objects.all().select_related('creator')[:10]
    return render(request, 'home.html', context={'name': 'eyad', 'events': query_set, 'title': 'Home'})


def about(request):
    return render(request, 'about.html', context={'title': 'About'})
