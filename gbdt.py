import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print("URL is not found")
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.find_all("h1")
        # title = bsObj.h1
    except AttributeError as e:
        return None

    return title


titles = getTitle("http://www.pythonscraping.com/pages/page1.html")
if titles is None:
    print("Title could not be found")
else:
    for title in titles:
        print(title.text)




