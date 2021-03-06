from django.db import models


class ToiNews(models.Model):
    head_line = models.CharField(max_length=100, primary_key=True)
    link = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.head_line


class Weather(models.Model):
    city = models.CharField(max_length=100)
    temp = models.CharField(max_length=5)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.city + ' ' + self.temp


class Help(models.Model):
    help = models.CharField(max_length=100)

    def __str__(self):
        return self.help


class Youtube(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    video_id = models.CharField(max_length=100)
    views = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-views']
        
    def __str__(self):
        return self.title


class FreqCMD(models.Model):
    pass
