import requests
from bs4 import BeautifulSoup as bs


def get_news():
    url = 'http://timesofindia.indiatimes.com/'
    news = []

    try:
        res = requests.get(url)

        if res.status_code == 200:
            soup = bs(res.text, 'html.parser')

            for new in soup.find('ul', attrs={'class': 'list9'}).find_all('a'):
                href = url + str(new['href'])
                text = str(new.contents[0])

                if not text.startswith('<i'):
                    news.append(text + '\n' + href)

        return news

    except ConnectionError:
        pass
