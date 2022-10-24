# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#네이버에서 경제면 기사를 보는 경우의 URL주소
data ='https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101' 
req = urllib.request.Request(data, \
                                    headers = hdr)
data = urllib.request.urlopen(req).read()
soup = BeautifulSoup(data, 'html.parser')

#  <ul class="list_txt"> 
#    <ul class="list_txt"> 
#     <li> <a href="https://news.naver.com/main/read.nhn?mode=LSD&amp;mid=shm&amp;sid1=101&amp;oid=421&amp;aid=0004549034" class="nclicks(rig.secteco)" title="두산중공업 기사회생…文정부, 병주고 약주고">두산중공업 기사회생…文정부, 병주고 약주고</a> </li> 
#     <li> <a href="https://news.naver.com/main/read.nhn?mode=LSD&amp;mid=shm&amp;sid1=101&amp;oid=025&amp;aid=0002987943" class="nclicks(rig.secteco)" title="한진 경영권 오늘 '운명의 날'&middot;&middot;&middot;11.16% 뒤진 조현아 카드는?">한진 경영권 오늘 '운명의 날'&middot;&middot;&middot;11.16% 뒤진 조현아 카드는?</a> </li> 
#     <li> <a href="https://news.naver.com/main/read.nhn?mode=LSD&amp;mid=shm&amp;sid1=101&amp;oid=025&amp;aid=0002988094" class="nclicks(rig.secteco)" title="달라지는 코로나 대출…신용등급 알아야 헛걸음 안 해요">달라지는 코로나 대출…신용등급 알아야 헛걸음 안 해요</a> </li> 
#     <li> <a href="https://news.naver.com/main/read.nhn?mode=LSD&amp;mid=shm&amp;sid1=105&amp;oid=421&amp;aid=0004549041" class="nclicks(rig.secteco)" title="'코로나19'로 위축된 스마트폰 시장…중저가 스마트폰 '승부수'">'코로나19'로 위축된 스마트폰 시장…중저가 스마트폰 '승부수'</a> </li> 
#     <li> <a href="https://news.naver.com/main/read.nhn?mode=LSD&amp;mid=shm&amp;sid1=105&amp;oid=293&amp;aid=0000027375" class="nclicks(rig.secteco)" title="엔씨, 코로나19 피해 PC방 지원 1개월 더">엔씨, 코로나19 피해 PC방 지원 1개월 더</a> </li> 
#    </ul> 
list = soup.select('ul > ul')
for item in list:
        try:
                title = item.find('a').text            
                print(title.strip())
        except:
                pass
        
