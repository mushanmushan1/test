import sys
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

# # data = requests.get("https://www.baidu.com/").content
# data = requests.get("http://www.pythonscraping.com/pages/page1.html").content
#
# soup = BeautifulSoup(data, "html.parser")
# print(soup.title.text)
# sys.exit(0)
#
# links = soup.find_all("a")
#
# for link in links:
#     print(link.string)


def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print("URL is not found")
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.h1
    except AttributeError as e:
        return None

    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title is None:
    print("Title could not be found")
else:
    print(title.text)




