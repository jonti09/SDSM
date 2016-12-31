#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import requests

url = 'https://www.youtube.com/feed/trending'
trending = []


def get_trendings():
	req = requests.get(url)

	if req.status_code == 200:
		soup = bs(req.text, 'html.parser')
		trendings = soup.find_all('a', attrs={'class': 'yt-uix-tile-link'})
		views = soup.find_all('ul', attrs={'class': 'yt-lockup-meta-info'})
				
		for trend, view in zip(trendings, views):
			data = trend.contents[0] + '	<small>' + view.contents[1].contents[0] + '</small>'
			trending.append(data)

	return trending
