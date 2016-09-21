from django.shortcuts import render


def sleep(request):
    return render(request, 'sleep.html')
