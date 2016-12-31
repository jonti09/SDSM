from django.conf.urls import url
from Data import views

urlpatterns = [

    url(r'^$', views.index, name='home'),

    url(r'^news/$', views.news, name='news'),

    url(r'^yesterday/$', views.yesterday, name='yesterday'),

    url(r'^help/', views.help, name='help'),

    url(r'^sleep/', views.sleep),

    url(r'^youtube/(?P<url>\w+)', views.youtube),

    url(r'^map/', views.maps),

]
