from django.shortcuts import render
from .models import ToiNews, Weather, Help, Youtube, FreqCMD
from datetime import datetime, timedelta
from .data.music import music


def index(request):
    slug = {
        'weather': Weather.objects.all().order_by('-date')[:1],
    }
    return render(request, 'home.html', slug)


def news(request):
    slug = {
        'news_list': ToiNews.objects.all().order_by('-date')[:10],
        'weather': Weather.objects.all().order_by('-date')[:1],
    }
    return render(request, 'news.html', slug)


def yesterday(request):
    slug = {
        'news_list': ToiNews.objects.filter(date__lte=(datetime.now() - timedelta(days=1)))[:10],
        'weather': Weather.objects.all().order_by('-date')[:1],
    }
    return render(request, 'news_yesterday.html', slug)


def help(request):
    slug = {
        'weather': Weather.objects.all().order_by('-date')[:1],
    }
    return render(request, 'help.html', slug)


def sleep(request):
    return render(request, 'sleep.html')


def maps(request):
    weather = Weather.objects.all().order_by('-date')[:1]
    city = request.GET.get('city')
    if city == '':
        slug = {
            'weather': weather,
            'error': 'No city specified',
        }
        return render(request, 'map.html', slug)
    slug = {
        'city': city,
        'weather': weather,
    }
    return render(request, 'map.html', slug)


def youtube(request, url):
    weather = Weather.objects.all().order_by('-date')[:1]
    if url == 'trending':
        slug = {
            'urls': Youtube.objects.order_by('-views')[:5],
            'weather': weather,
        }
        return render(request, 'youtube_trending.html', slug)
    else:
        slug = {
            'url': Youtube.objects.all().order_by('-views')[int(url) - 1],
            'weather': weather,
        }
        return render(request, 'youtube_player.html', slug)


def songs(request):
    action = str(request.GET.get('action'))
    num = int(request.GET.get('num'))

    if action == 'play':
        music.play_song(action, num)
    
    elif action == 'list':
        pass
    
    else:
        music.play_song(action, num)

    slug = {
        'weather': Weather.objects.all().order_by('-date')[:1],
        'songs': music.get_songs(),
    }
    return render(request, 'music_list.html', slug)
