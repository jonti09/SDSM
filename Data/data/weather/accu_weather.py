from bs4 import BeautifulSoup as bs
import requests


def get_weather():

    try:
        req = requests.get('http://www.accuweather.com/en/in/anand/188164/weather-forecast/188164')

        if req.status_code == 200:
            soup = bs(req.content, 'html.parser')

            temp = soup.find('div', attrs={'id': 'feed-tabs'})\
                       .find('span', attrs={'class': 'large-temp'})

            return str(temp.text)

    except ConnectionError:
        pass
