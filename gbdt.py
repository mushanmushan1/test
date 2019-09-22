import sys
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

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

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.h1)




