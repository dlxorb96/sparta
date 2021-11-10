import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://comic.naver.com/webtoon/weekday',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작

# content > div.list_area.daily_all > div:nth-child(5) > div > ul > li:nth-child(3)
#content > div.list_area.daily_all > div:nth-child(5) > div > ul > li:nth-child(3) > a
webtoons = soup.select('#content > div.list_area.daily_all > div:nth-child(5) > div > ul > li')

for webtoon in webtoons:
    title = webtoon.select_one('.title').text
    print(title)





