import sys
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


def getlinks(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print("URL is not found")
        return None

    try:
        bsObj = BeautifulSoup(html, "html.parser")
        links = bsObj.find_all("a")  # 获取 web页面链接

    except AttributeError as e:
        print("bsObj fails")
        return None

    return links


links = getlinks("https://en.wikipedia.org/wiki/Kevin_Bacon")

if links == None:
    print("Links could not be found")
else:
    for link in links:
        if "href" in link.attrs:
            print(link.attrs['href'])




