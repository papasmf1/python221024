#Query 
from pandas import DataFrame

data = [
    {"cd":"A060310", "nm":"3S", "open":2920, "close":2800},
    {"cd":"A095570", "nm":"AJ네트웍스", "open":1920, "close":1900},
    {"cd":"A006840", "nm":"AK홀딩스", "open":2020, "close":2010},
    {"cd":"A054620", "nm":"APS홀딩스", "open":3120, "close":3200}
]
df = DataFrame(data=data)
df = df.set_index('cd')
print(df)

#불린형 데이터가 담긴 조건 시리즈로 슬라이싱해서 시가가 2,000이상인 값만 선택
cond = df['open'] >= 2000
print(df[cond])

# 이번에는 데이터프레임의 query 메서드로 필터링해봅시다. 
# 쿼리라고 불리는 특수한 명령을 query 메서드로 전달해주면 됩니다. 
# 큰따옴표로 전체 쿼리를 정의하고 쿼리 안에서 사용하는 문자열은 작은따옴표로 구분합니다.
# 혹은 반대로 작은따옴표로 쿼리를 묶고 큰따옴표로 문자열을 구분할 수도 있습니다. 
# 컬럼과 인덱스는 따옴표 없이 사용할 수 있습니다. 
# 다음은 nm이라는 컬럼에서 3S라는 값을 갖는 데이터를 필터링합니다.
print(df.query("nm=='3S'"))
print(df.query('nm=="3s"'))

#크다와 작다를 다음과 같이 비교한다.
print(df.query("open > close"))

#in연산자는 뒤에 나오는 자료구조에 나열된 데이터만 선택한다.
print(df.query("nm in ['3S', 'AK홀딩스']"))

#인덱스를 기준으로 조회
print(df.query("cd == 'A060310'"))

#@키워드를 사용해서 변수를 참조할 수 있다. 
name = "AJ네트웍스"
print(df.query('nm == @name'))

#필터
# query 메서드가 값을 사용해서 필터링 할 수 있었다면 
# filter 메서드는 인덱스나 컬럼 이름에 대해서 특정 조건으로 
# 필터링할 수 있습니다. 
# 예제로 사용할 데이터프레임을 우선 정의해 보겠습니다.
from pandas import DataFrame

data = [
    [1416, 1416, 2994, 1755],
    [6.42, 17.63, 21.09, 13.93],
    [1.10, 1.49, 2.06, 1.88]
]

columns = ["2018/12", "2019/12", "2020/12", "2021/12(E)"]
index = ["DPS", "PER", "PBR"]

df = DataFrame(data=data, index=index, columns=columns)
print(df)

# filter 메서드의 items 파라미터로 선택할 컬럼의 이름을 
# 지정할 수 있습니다. 
# 여러 개의 이름을 입력하면 나열한 모든 컬럼이 선택됩니다.
print(df.filter(items=['2018/12']))

# 인덱스에 대해서도 필터링을 할 수 있습니다. 
# axis 파라미터를 0으로 설정하면 인덱스에 대해 검색하라는 뜻입니다. 
# 다음 코드는 인덱스에서 PER을 찾아 그림 5.2.3과 같은 데이터프레임을 반환합니다. axis를 입력하지 않으면 1로 설정되어 컬럼에서 탐색합니다.
print(df.filter(items=["PER"], axis=0))

# 여러 종목에 대해서 백테스팅을 수행할 때 회사별로 결산월이 다릅니다. 
# 이 경우 컬럼에서 2020이라는 문자열 일부로 필터링하는 것이 필요합니다. 
# regex 파라미터는 정규표현식을 사용할 수 있습니다.
print(df.filter(regex="2020"))

#^2020은 2020으로 시작하는 문자열 패턴만 찾으라는 뜻이다.
print(df.filter(regex="^2020"))

#R$는 R로 끝나는 모든 패턴을 의미 
print(df.filter(regex="R$", axis=0))

# 배운 것을 응용해 봅시다. 숫자 네 개와 '/' 그리고 숫자 두 개로 
# 구성된 컬럼을 선택하는 정규식을 작성해 보겠습니다. 
# 즉, E가 붙은 추정치를 제외하고 확정된 지표만을 선택하는 겁니다.
print(df.filter(regex="\d{4}/\d{2}$"))

#정렬 및 순위 
# 이번 절에서는 데이터프레임을 정렬하고 순위를 매겨 보겠습니다. 
# 데이터프레임에 정렬 및 순위를 매기는 것은 기본적으로 시리즈 객체와 동일합니다. 
# 우선 다음과 같이 예제로 사용할 데이터프레임을 생성합니다.
from pandas import DataFrame

data = [
    ["037730", "3R", 1510],
    ["036360", "3SOFT", 1790],
    ["005670", "ACTS", 1185]
]

columns = ["종목코드", "종목명", "현재가"]
df = DataFrame(data=data, columns=columns)
df.set_index("종목코드", inplace=True)

# 데이터프레임 객체는 여러 개의 컬럼으로 구성되기 때문에 시리즈와 달리 
# 정렬 기준을 정해줘야 합니다. '현재가' 컬럼을 기준으로 정렬해 봅시다.
df2 = df.sort_values("현재가")
print(df2)

#파라메터의 이름을 지정할 수도 있다.
df2 = df.sort_values(by="현재가")
print(df2)

#내림차순으로 지정할 경우라면 
df2 = df.sort_values(by="현재가", ascending=False)
print(df2)

# 이번에는 '현재가'가 낮은 종목부터 순위를 매겨 보겠습니다. 
# 이를 위해 데이터프레임에서 '현재가' 컬럼을 선택한 후 rank 메서드를 호출합니다.
# rank 메서드는 순위가 저장된 시리즈 객체를 리턴합니다. 
# 그래서 아래와 같이 순위를 매긴 후에 해당 컬럼을 
# 기존의 데이터프레임에 추가하는 것이 데이터 관리에 편리합니다.
df['순위'] = df['현재가'].rank()
print(df)

#순위별로 정렬하려면 아래와 같이 한다.
df.sort_values(by="순위", inplace=True)
print(df)

#인덱스 연산 
import pandas as pd 

idx1 = pd.Index([1,2,3])
idx2 = pd.Index([2,3,4])
print(type(idx1))

#중복을 제거하고 유니크하게 만들면
print(idx1.union(idx2))

#중복된 데이터만 선택한다면
print(idx1.intersection(idx2))

#차집합
print(idx1.difference(idx2))


#Groupby 
# 우선 "2차전지(생산)", "해운", "시스템반도체"의 세 그룹으로 
# 종목을 분류해야 합니다. 
# 다음 코드는 조건 비교를 사용해서 테마 컬럼이 "2차전지(생산)"와 같은 
# 종목만 필터링합니다.
from pandas import DataFrame

data = [
    ["2차전지(생산)", "SK이노베이션", 10.19, 1.29],
    ["해운", "팬오션", 21.23, 0.95],
    ["시스템반도체", "티엘아이", 35.97, 1.12],
    ["해운", "HMM", 21.52, 3.20],
    ["시스템반도체", "아이에이", 37.32, 3.55],
    ["2차전지(생산)", "LG화학", 83.06, 3.75]
]

columns = ["테마", "종목명", "PER", "PBR"]
df = DataFrame(data=data, columns=columns)
df1 = df[df['테마'] == "2차전지(생산)"]
print(df1)

#해운과 시스템반도체 테마도 필터링을 한다.
df2 = df[df['테마'] == "해운"]
df3 = df[df['테마'] == "시스템반도체"]

#이번에는 테마별로 그룹화한 데이터프레임 객체에서 평균값 계산
mean1 = df1['PER'].mean()
mean2 = df2['PER'].mean()
mean3 = df3['PER'].mean()

#테마별로 PER의 평균을 시리즈로 저장한다. 
data = [mean1, mean2, mean3]
index = ["2차전지(생산)","해운", "시스템반도체"]
s = pd.Series(data=data, index=index)
print(s)

# 여러분이 지금까지 한 작업을 보면 먼저 테마별로 분할(Split)을 한 후 
# 각 테마에 대해서 평균 연산을 반영(Apply)했고 마지막으로 
# 결과를 결합(Combine) 함으로써 테마별 평균 PER이라는 데이터를 
# 집계하였습니다. 
# 데이터프레임은 이러한 데이터 집계 연산을 쉽게 처리할 수 있는 
# groupby 메서드를 제공합니다. 
# 앞서 여러분이 작성했던 코드는 다음과 같이 간소화될 수 있습니다.
print(df.groupby("테마")["PER"].mean())
 

# groupby 메서드는 분할(Split)을 담당하며 DataFrameGroupBy라는 
# 타입의 객체를 리턴합니다. 
# DataFrameGroupBy 객체의 get_group 메서드로 특정한 값을 갖는 
# 데이터프레임을 얻을 수 있습니다. 
# 다음은 "2차전지(생산)" 테마의 데이터만을 선택합니다.
gb = df.groupby("테마")
temp = gb.get_group("2차전지(생산)")
print(temp)

#  중에서 종목명을 제외하고 PER과 PBR만을 선택해 봅시다. 
# 원본 데이터를 슬라이싱해서 필요한 세 개의 컬럼에 groupby 메서드를 
# 적용할 수 있습니다.
temp = df[["테마","PER","PBR"]].groupby("테마").get_group("2차전지(생산)")
print(temp)

# 새롭게 소개할 방법은 DataFrameGroupBy 객체를 슬라이싱합니다. 
# DataFrameGroupBy 객체는 데이터프레임과 유사하게 컬럼 인덱싱과 슬라이싱을 
# 지원합니다. 테마별로 정리한 DataFrameGroupBy 객체에서 PER과 PBR 컬럼만을 
# 선택한 뒤 "2차전지(생산)"이 포함된 테마만을 선택합니다.
temp = df.groupby("테마")[ ["PER","PBR"] ].get_group("2차전지(생산)")
print(temp)

# 여러 개의 컬럼에 집계 기능까지 연결해 보겠습니다. 
# groupby 메서드로 그룹화하고 PER과 PBR 컬럼에 mean 메서드를 적용합니다. 
# mean 연산이 적용되고 그룹별 결과를 하나로 합쳐서 데이터프레임을 반환합니다.
print(df.groupby("테마")[["PER","PBR"]].mean())

# 하지만 groupby 메서드는 PER과 PBR을 슬라이싱하지 않더라도 
# 평균 연산을 적용할 수 없는 "종목명" 컬럼을 자동으로 제거하고 
# 아래의 데이터프레임을 반환합니다.
print(df.groupby("테마").mean())

# 데이터프레임을 그룹화한 후 특정 컬럼마다 다른 함수를 적용할 수 있습니다. 
# 예를 들어 PER의 max, PBR의 min을 해당 그룹의 대푯값으로 설정하고자 하는 경우 
# 다음과 같이 agg 메서드를 사용합니다. 
# 컬럼의 이름을 key, 적용할 함수의 이름을 value로 전달할 수 있습니다.
print(df.groupby("테마").agg({"PER":max, "PBR":min}))

# 하나의 컬럼에 여러 연산을 지정할 수도 있습니다. 
# 딕셔너리의 value에 리스트로 적용할 연산을 나열합니다. 
# PER에는 파이썬이 제공하는 기본 함수 min과 max, 
# PBR에는 numpy가 제공하는 표준편차와 분산을 구합니다.
import numpy as np 
print(df.groupby("테마").agg({"PER":[min,max],
                            "PBR":[np.std, np.var]}))