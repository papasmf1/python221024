import urllib.request
from bs4 import BeautifulSoup
data = urllib.request.urlopen('http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri')
soup = BeautifulSoup(data, 'html5lib')
soup
