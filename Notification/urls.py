from django.conf.urls import url
from django.views.generic import ListView
from Notification.models import ToiNews, Weather, Help
from Notification.views import sleep
from datetime import datetime, timedelta


urlpatterns = [

    url(r'^$',
        ListView.as_view(queryset=ToiNews.objects.all().order_by('-date')[:10], template_name='notification.html')),

    url(r'^yesterday/$',
        ListView.as_view(queryset=ToiNews.objects.filter(date__lte=(datetime.now() - timedelta(days=1)))[:10],
                         template_name='news_pre.html', )),

    url(r'weather/',
        ListView.as_view(queryset=Weather.objects.all().order_by('-date')[:1], template_name='weather.html')),

    url(r'help', ListView.as_view(queryset=Help.objects.all(), template_name='help.html')),

    url(r'^sleep', sleep),
]