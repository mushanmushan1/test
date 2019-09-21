import sys
import requests
from bs4 import BeautifulSoup


baidu = requests.get("https://www.baidu.com/").content
# print(baidu)

soup = BeautifulSoup(baidu, "html.parser")
print(soup.text)
# sys.exit(0)

links = soup.find_all("a")

for link in links:
    print(link.string)

