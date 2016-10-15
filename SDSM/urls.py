from django.conf.urls import url, include
from django.contrib import admin
from SDSM import task

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^notification/', include('Data.urls')),
]

task.insert_toi()
task.weather()
