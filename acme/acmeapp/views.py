from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Home, About, Service

# Create your views here.

def index(request):
    index = get_object_or_404(Home, pk=1)
    index2 = get_object_or_404(Home, pk=2)
    index3 = get_object_or_404(Home, pk=3)
    print(index.box_image)
    return render(request, 'index.html', {
        'index': index,
        'index2': index2,
        'index3': index3,
    })

def about(request):
    about = get_object_or_404(About, pk=1)
    return render(request, 'about.html', {
        'about': about,
    })

def services(request):
    service = get_object_or_404(Service, pk=1)
    service2 = get_object_or_404(Service, pk=2)
    service3 = get_object_or_404(Service, pk=3)
    return render(request, 'services.html', {
        'service': service,
        'service2': service2,
        'service3': service3,
    })
