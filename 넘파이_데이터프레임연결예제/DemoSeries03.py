#시리즈 정렬
from pandas import Series 

data = [3.1, 2.0, 10.1, 5.1]
index = ['000010', '000020', '000030', '000040']
s = Series(data=data, index=index)
print(s)

#오른차순 정렬
s1 = s.sort_values()
print(s1)

#내림차순
s2 = s.sort_values(ascending=False)
print(s2)

#시리즈 객체에는 순위를 매기는 rank메서드가 있다. 
#기본적으로 값이 작은 데이터를 1순위로 지정한다.
data = [3.1, 2.0, 10.1, 3.1]
index = ['000010','000020','000030','000040']
s = Series(data=data, index=index)
print(s.rank())

#만약 값이 큰 데이터를 1등으로 순위를 매기려면 
print(s.rank(ascending=False))
