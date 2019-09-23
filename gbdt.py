import sys
import re       # 正则表达
import random
import datetime
import requests
from bs4 import BeautifulSoup
from scrapy import Item, Field
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


# def getlinks(url):
#     try:
#         html = urlopen(url)
#     except (HTTPError, URLError) as e:
#         print("URL is not found")
#         return None
#
#     try:
#         bsObj = BeautifulSoup(html, "html.parser")
#
#         # 获取 web页面链接
#         links = bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
#     except AttributeError as e:
#         print("bsObj fails")
#         return None
#
#     return links
#
# links = getlinks("https://en.wikipedia.org/wiki/Kevin_Bacon")
#
# if links == None:
#     print("Links could not be found")
# else:
#     for link in links:
#         if "href" in link.attrs:
#             print(link.attrs['href'])

random.seed(datetime.datetime.now())


def getLinks(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print("URL is not found")
        return None

    try:
        bsObj = BeautifulSoup(html, "html.parser")
        links = bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    except AttributeError as e:
        print("bsObj fails!")
        return None

    return links


links = getLinks("https://en.wikipedia.org/wiki/Kevin_Bacon")

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)

    links = getLinks(newArticle)




