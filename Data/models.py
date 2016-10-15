from django.db import models


class ToiNews(models.Model):
    head_line = models.CharField(max_length=100, primary_key=True)
    link = models.CharField(max_length=140)
    date = models.DateTimeField()

    def __str__(self):
        return self.head_line


class Weather(models.Model):
    city = models.CharField(max_length=100)
    temp = models.CharField(max_length=5)
    date = models.DateTimeField()


class Help(models.Model):
    help = models.CharField(max_length=100)

    def __str__(self):
        return self.help
