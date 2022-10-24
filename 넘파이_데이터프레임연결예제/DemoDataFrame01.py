from pandas import DataFrame

data = {
    '종목코드':['037730','036360','005760'],
    '종목명':['3R','3SOFT','ACTS'],
    '현재가':[1510,1790,1185]
}

df = DataFrame(data)
print(df)

#컬럼순서 지정
columns = ['종목코드','종목명','현재가']
df2 = DataFrame(data=data, columns=columns)
print(df2)

#데이터프레임의 인덱스
data = [
    ["037730", "3R", 1510, 7.36],
    ["036360", "3SOFT", 1790, 1.65],
    ["005670", "ACTS", 1185, 1.28]
]

columns = ["종목코드", "종목명", "현재가", "등락률"]
df = DataFrame(data=data, columns=columns)
print(df)

#종목코드 컬럼을 인덱스로 지정할 수 있다. 
#이런 경우 set_index메서드를 사용한다. 
data = [
    ["037730", "3R", 1510, 7.36],
    ["036360", "3SOFT", 1790, 1.65],
    ["005670", "ACTS", 1185, 1.28]
]

columns = ["종목코드", "종목명", "현재가", "등락률"]
df = DataFrame(data=data, columns=columns)
df = df.set_index("종목코드")
print(df)

#set_index메서드를 호출할 때 
#inplace값을 True로 전달하면 수정사항을 직접 
#반영할 수 있다.
#df.set_index("종목코드", inplace=True)

#인덱스를 다음과 같이 별도로 지정할 수 있다. 
data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730","036360","005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index,
    columns=columns)
df.index.name = "종목코드"
print(df)

#컬럼 인덱싱
data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)
print(df['현재가'])


#여러개의 컬럼을 한번에 슬라이싱할 수 있다. 
리스트 = ["현재가","등락률"]
print(df[리스트])

#간단하게 한줄로 표현
print(df[ ["현재가","등락률"] ])

#데이터프레임에서 한개의 열만 인덱싱하면 시리즈 객체이다.
#하지만 다음과 같이 리스트로 슬라이싱하면 데이터프레임이다.
#데이터프레임만 지원하는 메서드를 사용한다면 유용하다.
print(df[ ["현재가"] ])


#로우 인덱싱
data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)
print(df.loc["037730"])

#데이터프레임에서 iloc속성을 사용하면 
#행번호로 로우 데이터를 인덱싱할 수 있다. 
#첫번째행과 마지막행을 출력
print(df.iloc[0])
print(df.iloc[-1])

#데이터프레임의 경우 슬라이싱 또는 불연속적인 여러 값을
#슬라이싱할 수 있다. 
#loc는 인덱스를 리스트로 전달하고, iloc는 행번호를
#리스트로 전달하면 된다. 
print(df.loc[ ['037730','036360']])
print(df.iloc[ [0,1] ])


#특정값을 가져오기 
data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

print(df.iloc[0])
print(df.loc['037730'])

#loc속성에 로우 인덱스와 컬럼명을 순서대로 입력하면 
#특정 로우와 컬럼에 위치하는 값을 한번에 가져올 수 있다.
print(df.loc['037730','현재가'])
#[행,열]과 같이 지정해서 읽어온다. 
print(df.iloc[0,1])

#특정범위를 지정하기
data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

print(df.loc[["037730","036360"]])
print(df.iloc[[0,1]])

#두번의 슬라이싱을 하는 것보다는(대용량의 데이터를 처리할 때 실행 성능저하의 문제)
#한번에 슬라이싱하는 것이 좋다. df.loc[[행],[열]] 
#또는 df.iloc[ [행번호],[열번호]]
print(df.loc[["037730","036360"], ["종목명","현재가"]])
print(df.iloc[[0,1], [0,1]])


#필터링
data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, 
    index=index, columns=columns)
cond = df['현재가'] >= 1400
print(df.loc[cond])

#반환된 데이터프레임에서 하나의 컬럼만 가져오고 싶다면
#컬럼의 이름으로 인덱싱을 할 수 있다.
cond = df["현재가"] >= 1400
print(df.loc[cond]["현재가"])
print(df.loc[cond, "현재가"])

#복잡한 조건을 기술할 때는 &(and), |(or), ~(not)연산자를 사용 
#예를 들면 1400이상이면서 1700미만인 조건의 값을 필터링 
cond = (df['현재가'] >= 1400) & (df['현재가'] < 1700)
print(df.loc[cond])

#반대의 경우라면
cond = (df['현재가'] >= 1400) & (df['현재가'] < 1700)
print(df.loc[~cond])


#컬럼을 추가하는 경우
from pandas import Series, DataFrame

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

#목표가 컬럼 추가
s = Series(data=[1600,1600,1600],
    index=df.index)
df['목표가'] = s
print(df)

#시리즈로 값을 구성하는 과정없이 추가될 컬럼의 이름과 
#추가할 데이터만 대입해도 같은 결과를 얻을 수 있다. 
#데이터프레임이 제공하는 편의 기능이다.
df['목표가2'] = 1600
print(df)

#괴리율을 추가한다. 
df['괴리율'] = (df['목표가'] - df['현재가']) / df['현재가']
print(df)


#로우를 추가하기
from pandas import DataFrame

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

#추가할 로우를 하나의 시리즈로 표현한다.
s = Series(data=['LG전자', 60000, 3.84], index=df.columns)
df.loc["066570"] = s 
print(df)

#다음과 같이 loc속성으로 066570이름의 인덱스에 데이터를 입력한다. 
#이 경우 데이터프레임이 우변에 있는 리스트를 시리즈로 변경하고 
#데이터프레임과 같은 컬럼 레이블을 갖도록 자동 변환한다. 
df.loc["066570"] = ["LG전자",60000,3.84]
print(df)

#append메서드로 추가한다. 
s = Series(data=["LG전자",60000,3.84],
    index=df.columns, name="066570")
new_df = df.append(s)
print(new_df)