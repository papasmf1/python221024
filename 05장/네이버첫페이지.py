#-*- coding: utf-8 -*-
# naver new
import urllib
from bs4 import BeautifulSoup
from datetime import datetime

soup = BeautifulSoup(urllib.request.urlopen('http://www.naver.com').read(), 'html5lib')
editData = soup.find_all('a', {'class': "newssa"})

#print editData
editDataStr = str(editData)
editDataStr = editDataStr.replace('[','')
editDataStr = editDataStr.replace(']','')
editDataStr = editDataStr.replace('"','')
editDataStr = editDataStr.replace('<a class=",">','')
editDataStr = editDataStr.replace('src=http://img.naver.net/static/newsstand/up/2014/0715/','')
editDataStr = editDataStr.replace('target=_blank&gt;<img alt="," />','')
editDataStr = editDataStr.replace(', ','\n')
editDataStr = editDataStr.replace('href=','')
editDataStr = editDataStr.replace('.gif/&gt;','')
editDataStr = editDataStr.replace('src=http://img.naver.net/static/newsstand/up/2015/0424/nsd163650137','')
editDataStr = editDataStr.replace('src=http://img.naver.net/static/newsstand/up/2015/0713/nsd145758454.png/&gt;','')
editDataStr = editDataStr.replace('src=http://img.naver.net/static/newsstand/up/2015/0303/nsd152544150','')
editDataStr = editDataStr.replace('src=http://img.naver.net/static/newsstand/up/2015/0707/nsd105132418','')
editDataStr = editDataStr.replace('src=http://img.naver.net/static/newsstand/up/2014/0912/nsd144736648','')

print(editDataStr)

setLines = editDataStr.splitlines() #editDataStr 변수 안에 있는 데이터를 한 줄씩 분리해서 setLines에 저장
for line in setLines: #setLines를 한 줄씩 읽어서 line변수에 넣는다.
	line = line[4:] #line의 앞에 4글자를 잘라낸다.
	space = line.rfind(' ') #뒤에서부터 공백이 있는 문자열의 인덱스를 찾아 변수에 저장한다.
	line = line[:space] #찾아낸 문자열 인덱스 뒤로 다 잘라낸다.
	print(line)
