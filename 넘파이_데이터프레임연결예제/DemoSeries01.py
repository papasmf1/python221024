from pandas import Series 
import numpy as np 

data = [10,20,30]
s = Series(data)
print(s)

#넘파이로 시리즈를 생성한다.
data = np.arange(5)
s = Series(data)
print(s)

#문자열 데이터도 저장할 수 있다.
data = ['시가','고가']
s = Series(data)
print(s)

#시리즈는 RangeIndex타입으로 0부터 숫자값이 생성된다.
data = [1000, 2000, 3000]
s = Series(data)
print(s.index)
print(s.index.to_list())


#인덱스를 다음과 같이 수정할 수 있다.
data = [1000, 2000, 3000]
s = Series(data)
s.index = ["메로나","구구콘","하겐다즈"]
print(s)

#아래와 같이 인덱스를 같이 지정하면 된다. 
data = [1000, 2000, 3000]
index = ["메로나","구구콘","하겐다즈"]
s = Series(data, index)
print(s)

#reindex메서드를 사용하면 인자로 전달된 
#새로운 값으로 맞추어 인덱스를 변경한다. 
#이때 기존에 있던 인덱스는 기존 값을 그대로
#사용하고 새로운 인덱스에는 NaN값을 채운다.
data = [1000, 2000, 3000]
index = ["메로나","구구콘","하겐다즈"]
s = Series(data=data, index=index)
s2 = s.reindex(["메로나","비비빅","구구콘"])
print(s2) 

#NaNa을 0으로 변경할 때는 fillna메서드를 사용할 수 있다. 
print(s2.fillna(0))

#reindex메서드를 사용할 때 fill_value파라메터를 사용해서 한번에 
#처리할 수도 있다. 
s2 = s.reindex(["메로나","비비빅","구구콘"], fill_value=0)
print(s2)

#삼성전자 종가를 저장한다.
price = [42500, 42550, 41800, 42550, 42650]
date = ["2019-05-31","2019-05-30","2019-05-29","2019-05-28",
        "2019-05-27"]
s = Series(price, date)
print(s)

#딕셔너리를 통해서 시리즈를 한번에 만들수도 있다.
data = {
    "2019-05-31" : 42500,
    "2019-05-30" : 42550,
    "2019-05-29" : 41800,
    "2019-05-28" : 42550,
    "2019-05-27" : 42650
}
s = Series(data)

print(s.index)
print(s.index.dtype)
print(s.values)

#시리즈의 인덱싱
data = [1000, 2000, 3000]
s = Series(data=data)

#iloc는 양수와 음수를 모두 사용할 수 있다. 
print(s.iloc[0])
print(s.iloc[1])
print(s.iloc[2])
print(s.iloc[-1])

#문자열 인덱스가 설정된 시리즈 객체에 대해서 
#loc연산은 인덱스를 iloc는 행번호를 사용한다는 것을 
#기억하면 된다. 
data = [1000, 2000, 3000]
index = ["메로나","구구콘","하겐다즈"]
s = Series(data=data, index=index)

print(s.iloc[0])
print(s.loc["메로나"])

#기본적으로 []기호는 내부적으로 loc메서드를 호출한다. 
s1 = Series([10,20,30])
s2 = Series([10,20,30], index=[1,2,3])
#0번 인덱스가 있으므로 정상 출력 
print(s1[0])
#0번이 없기 때문에 에러 발생 
# print(s2[0])

# []기호는 편리하지만 개발자가 충분히 이해하지 못하고 사용하면
#문제를 일으킬 수 있다. 따라서 행번호를 사용하는 iloc나 인덱스를
#사용하는 loc를 명시하는 것이 좋다. 

#시리즈 슬라이싱
data = [1000, 2000, 3000]
index = ["메로나","구구콘","하겐다즈"]
s = Series(data=data, index=index)
print(s.iloc[0:2])

data = [1000, 2000, 3000]
index = ["메로나","구구콘","하겐다즈"]
s = Series(data=data, index=index)
print(s.loc["메로나":"구구콘"])

#앞서 iloc[0:2]라는 표현은 0번과 1번행을 데이터로 가져오고
#2번은 가져오지 않습니다. 이와 달리 loc연산은 끝인덱스도 
#포함해서 값을 가져옵니다.   

#시리즈객체는 파이썬 리스트와 달리 연속적이지 않은 값들에 
#대해서도 슬라이싱 할 수 있다. 
data = [1000, 2000, 3000]
index = ["메로나","구구콘","하겐다즈"]
s = Series(data=data, index=index)

indice = [0,2]
print(s.iloc[ indice ])
print(s.iloc[ [0,2] ])

