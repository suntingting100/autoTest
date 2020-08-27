from bs4 import BeautifulSoup
import requests
from urllib import request
import time

target_url = "http://top.baidu.com/buzz?b=1&fr=topindex"
r = requests.get(target_url).content
soup = BeautifulSoup(r, "html.parser")

t = soup.find_all(class_="list-title")
for i in t:
    try:
        title = i
        print(title)
    except:
        pass


