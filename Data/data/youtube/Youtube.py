#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import requests

url = 'https://www.youtube.com/feed/trending'
api_url = 'http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc'

req = requests.get(url)

if req.status_code == 200:
	soup = bs(req.text, 'html.parser')
	trendings = soup.find_all('a', attrs={'class': 'yt-uix-tile-link'})
	
	for trend in trendings:
		print(trend.contents[0])

