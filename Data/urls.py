from django.conf.urls import url
from django.views.generic import ListView
from Data.models import ToiNews, Weather
from Data import views
from datetime import datetime, timedelta

urlpatterns = [

    url(r'^$',
        ListView.as_view(queryset=Weather.objects.all().order_by('-date')[:1], template_name='home.html')),

    url(r'^news$',
        ListView.as_view(queryset=ToiNews.objects.all().order_by('-date')[:10], template_name='news.html')),

    url(r'^yesterday/$',
        ListView.as_view(queryset=ToiNews.objects.filter(date__lte=(datetime.now() - timedelta(days=1)))[:10],
                         template_name='news_yesterday.html')),

    url(r'weather/',
        ListView.as_view(queryset=Weather.objects.all().order_by('-date')[:1], template_name='weather.html')),

    url(r'^help/',
        ListView.as_view(queryset=Weather.objects.all().order_by('-date')[:1], template_name='help.html')),

    url(r'^sleep/', views.sleep),

    url(r'^map/', views.maps),

]
