from pandas import Series 

#시리즈 수정/추가/삭제
data = [1000,2000,3000]
index = ["메로나","구구콘","하겐다즈"]
s = Series(data=data, index=index)

s.loc["메로나"] = 500
print(s)

#iloc로도 수정할 수 있다. 
s.iloc[0] = 600

#시리즈에 인덱스가 존재하지 않으면 새로운 값이 입력
s.loc['비비빅'] = 500
print(s)

#삭제는 drop메서드를 사용
print(s.drop('메로나'))
#아래는 에러 발생 인덱스를 넘겨야 한다. 
#print(s.drop(0))

#drop메서드는 시리즈의 원본 데이터를 제거하지 않고 
#새로운 시리즈 객체를 반환하는 것에 유의해야 한다. 
#이는 실수로 원본 데이터를 수정하는 것을 방지하기 위한 일종의 안전장치이다. 
#drop메서드를 호출한 결과를 다시 변수에 바인딩해야 한다. 
s = s.drop('비비빅')
print(s)

#시리즈 연산
#같은 인덱스끼리 연산이 된다. 
철수 = Series([10,20,30], index=['NAVER','SKT','KT'])
영희 = Series([10,30,20], index=['SKT','KT','NAVER'])
가족 = 철수 + 영희 
print(가족)

#리스트와 다르게 브로드캐스팅이 된다.
print(철수 * 10)

#결과가 시리즈객체로 저장됨 
high = Series([42800, 42700, 42050, 42950, 43000])
low = Series([42150, 42150, 41300, 42150, 42350])

diff = high - low
print(diff)

#변동폭이 가장 큰 값은?
print(diff.max())

#날짜를 인덱스로 지정
date = ["6/1", "6/2", "6/3", "6/4", "6/5"]
high = Series([42800, 42700, 42050, 42950, 43000], index=date)
low = Series([42150, 42150, 41300, 42150, 42350] , index=date)
diff = high - low
print(diff)


#수익률 계산
date = ["6/1", "6/2", "6/3", "6/4", "6/5"]
high = Series([42800, 42700, 42050, 42950, 43000], index=date)
low = Series([42150, 42150, 41300, 42150, 42350] , index=date)
profit = high / low
print(profit)

#누적 수익률을 계산할 때 cumprod메서드를 사용하면 된다.
#모든 수익률을 누적해서 곱합으로 계산할 수 있는데 메서드를 사용한다. 
print(profit.cumprod())

#인덱싱으로 하나의 값을 가져온다. 
print(profit.cumprod().iloc[-1])


#데이터 개수를 카운트하는 방법을 학습해 본다.
data = {
    "삼성전자": "전기,전자",
    "LG전자": "전기,전자",
    "현대차": "운수장비",
    "NAVER": "서비스업",
    "카카오": "서비스업"
}
s = Series(data)

#중복을 제거하고 업종리스트 가져오기
print(s.unique())

#출현 빈도를 계산하고 싶으면 value_counts메서드 
print(s.value_counts())

#시리즈와 맵
#아래의 경우 ,때문에 에러발생 
s = Series(['1,234', '5,678', '9,876'])
#print(int(s))


def remove_comma(x):
    return int(x.replace(',', ''))

s = Series(['1,234', '5,678', '9,876'])
result = s.map(remove_comma)
print(result)

def is_greater_than_5000(x):
    if x > 5000:
        return '크다'
    else:
        return '작다'
    
s = Series([1234, 5678, 9876])
s = s.map(is_greater_than_5000)
print(s)

data = [42500, 42550, 41800, 42550, 42650]
index = ['2019-05-31','2019-05-30',
        '2019-05-29','2019-05-28','2019-05-27']
s = Series(data=data, index=index)
cond = s > 42000
print(cond)

#불리언 인덱싱을 할 경우 []연산자에 True, False가 저장된
#시리즈 객체를 넘겨주기만 하면 된다.
print(s[cond])

#이번에는 종가가 시가보다 큰지를 지정하면 된다. 
close = [42500, 42550, 41800, 42550, 42650]
open = [42600, 42200, 41850, 42550, 42500]
index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

open = Series(data=open, index=index)
close = Series(data=close, index=index)

cond = close > open
print(cond)

#종가가 시가보다 높앗던 상승 마감한 날의 종가를 출력하려면?
#앞에서 배운 불리언 색인 기능을 사용하면 된다. 
cond = close > open
print(close[cond])

#간단하게 한줄로 표현할 수 있다. 
print(close[close > open])
