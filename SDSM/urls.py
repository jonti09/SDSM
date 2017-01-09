from django.conf.urls import url, include
from django.contrib import admin
from SDSM import task

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('Data.urls')),
]
