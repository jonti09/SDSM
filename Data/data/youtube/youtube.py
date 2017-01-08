#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import requests

BASE_URL = 'https://www.youtube.com/feed/trending'


def get_trendings():
    trending = []
    req = requests.get(BASE_URL)
    if req.status_code == 200:
        soup = bs(req.text, 'html.parser')
        trendings = soup.find_all('a', attrs={'class': 'yt-uix-tile-link'})
        views = soup.find_all('ul', attrs={'class': 'yt-lockup-meta-info'})
        for trend, view in zip(trendings, views):
            try:
                title = str(trend.contents[0])
                video_id = str(trend['href']).split('?v=')[-1]
                views = str(view.contents[1].contents[0]).split(' ')[0]
                trending.append(title + '\n' + video_id + '\n' + views)
            except IndexError:
                pass
    return trending[:10]
