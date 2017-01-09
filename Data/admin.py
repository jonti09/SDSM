from django.contrib import admin
from Data.models import ToiNews, Weather, Help, Youtube


class ToiNewsAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'date']
	class Meta:
		model = ToiNews


class YoutubeAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'date', 'views']
	class Meta:
		model = Youtube


# Register your models here.
admin.site.register(ToiNews, ToiNewsAdmin)
admin.site.register(Weather)
admin.site.register(Help)
admin.site.register(Youtube, YoutubeAdmin)
