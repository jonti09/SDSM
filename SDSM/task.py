from Notification.models import ToiNews, Weather
from Notification.data.news import toi
from Notification.data.weather import accu_weather
from datetime import datetime


# TOI
def insert_toi():
    data = toi.get_news()

    t = ToiNews()

    for val in data:
        try:
            t.head_line = str(val).split('\n')[0]
            t.link = str(val).split('\n')[-1]
            t.date = datetime.now()
            t.save()
        except RuntimeWarning:
            pass


def weather():
    try:
        w = Weather()
        w.city = 'Anand'
        w.temp = accu_weather.get_weather()
        w.date = datetime.now()
        w.save()
    except RuntimeWarning:
        pass
