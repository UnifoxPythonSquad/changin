# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "http://www.melon.com/chart/index.htm"

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)'}
melon = requests.get(url, headers = header) # 멜론차트 웹사이트
melon_html = melon.text
melon_parse= BeautifulSoup(melon_html, 'html.parser')

list_name = []
list_author = []

titles = melon_parse.select('#lst50 > td > div > div > div.ellipsis.rank01 > span > a')
artists = melon_parse.select('#lst50 > td > div > div > div.ellipsis.rank02 > a')

for i in range(30):
    print(str(i+1)+' : '+titles[i].text+' - '+artists[i].text)