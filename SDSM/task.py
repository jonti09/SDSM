from Data.models import ToiNews, Weather, Youtube
from Data.data.news import toi
from Data.data.weather import accu_weather
from Data.data.youtube import youtube
from datetime import datetime


# TOI
def insert_toi():
    data = toi.get_news()

    t = ToiNews()

    try:
        for val in data:
            t.head_line = str(val).split('\n')[0]
            t.link = str(val).split('\n')[-1]
            t.date = datetime.now()
            t.save()
    except RuntimeWarning:
        pass

# Weather
def weather():
    try:
        w = Weather()
        w.city = 'Anand'
        w.temp = accu_weather.get_weather()
        w.date = datetime.now()
        w.save()
    except RuntimeWarning:
        pass


# Youtube Trendings
def trending():
    data = youtube.get_trendings()
    obj = Youtube()

    try: 
        for val in data:
            obj.title = str(val).split('\n')[0]
            obj.video_id = str(val).split('\n')[1]
            obj.views = str(val).split('\n')[-1]
            obj.date = datetime.now()
            obj.save()
    except RuntimeWarning:
        pass