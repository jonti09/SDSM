from django.shortcuts import render
from django.http import request


def sleep(request):
    return render(request, 'sleep.html')


def maps(request):
    city = {
        'city': request.GET.get('city', '')
    }
    return render(request, 'map.html', city)
