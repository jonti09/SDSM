from django.conf.urls import url
from django.views.generic import ListView
from Notification.models import ToiNews, Weather, Help
from Notification.views import sleep

urlpatterns = [
    url(r'^weather/',
        ListView.as_view(queryset=Weather.objects.all().order_by('-date')[:1], template_name='weather.html')),

    url(r'^$',
        ListView.as_view(queryset=ToiNews.objects.all().order_by('-date')[:10], template_name='notification.html')),

    url(r'^help', ListView.as_view(queryset=Help.objects.all(), template_name='help.html')),

    url(r'^sleep', sleep),
]