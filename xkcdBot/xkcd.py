from urllib import request
from urllib.error import HTTPError
import json
from random import randint


class xkcdComic(object):
    def __init__(self, comic_id: int):
        self.url = 'https://xkcd.com/{}'.format(comic_id)
        response = request.urlopen(self.url + '/info.0.json')
        site = response.read().decode("utf-8")
        data = json.loads(site)

        self.month = data['month']
        self.num = data['num']
        self.link = data['link']
        self.year = data['year']
        self.news = data['news']
        self.safe_title = data['safe_title']
        self.transcript = data['transcript']
        self.alt = data['alt']
        self.img = data['img']
        self.title = data['title']
        self.day = data['day']
        self.raw = data


def random_xkcd_comic():
    while True:
        try:
            random_comic_id = randint(1, 2000)
            # Todo: implement randint max number to be precise, lookup from RSS feed.
            return xkcdComic(random_comic_id)
        except HTTPError:
            pass


def comic_to_message(comic):
    return f"{comic.title}\n{comic.img}"


def random_comic_message():
    return comic_to_message(random_xkcd_comic())


if __name__ == '__main__':
    comic = xkcdComic(1903)
    print(random_comic_message())
    assert comic.title == 'Bun Trend'
    assert comic.img == 'https://imgs.xkcd.com/comics/bun_trend.png'
    assert comic.url == 'https://xkcd.com/1903'
    assert comic_to_message(comic) == f"{comic.title}\n{comic.img}"
