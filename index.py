import requests
from bs4 import BeautifulSoup

url = "https://datalab.naver.com/keyword/realtimeList.naver?where=main"
headers = { 'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')}
source = requests.get(url, headers=headers).text

soup = BeautifulSoup(source, "html.parser")
hotKeys = soup.select("div.list_group span.item_title")

index = 0
for key in hotKeys:
    index += 1
    print(str(index) + ", " + key.text)
    if index >= 20:
        break
