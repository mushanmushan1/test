import requests
from bs4 import BeautifulSoup


baidu = requests.get("https://www.baidu.com/").content
# print(baidu)

soup = BeautifulSoup(baidu, "html.parser")
# print(soup)

links = soup.find_all("a")

for link in links:
    print(link.string)

