from django.shortcuts import render
from django.http import request
from .data.youtube.Youtube import get_trendings
from .models import ToiNews, Weather, Help
from datetime import datetime, timedelta


def index(request):
	slug = {
		'weather': Weather.objects.all().order_by('-date')[:1],
	}
	return render(request, 'home.html', slug)


def news(request):
	slug = {
		'news': ToiNews.objects.all().order_by('-date')[:10],
		'weather': Weather.objects.all().order_by('-date')[:1],
	}
	return render(request, 'news.html', slug)


def yesterday(request):
	slug = {
		'news': ToiNews.objects.filter(date__lte=(datetime.now() - timedelta(days=1)))[:10],
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
			'urls': get_trendings()[:5], 
			'weather': weather,
		}
		return render(request, 'youtube.html', slug)
	else:
		slug = {
			'error': 'Nothing to iter over', 
			'weather': weather,
		}
		return render(request, 'youtube.html', slug)