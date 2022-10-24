#Stack/Unstack
from pandas import DataFrame
import pandas as pd 

data = [
    [1000,900,800,700],
    [1200,1400,900,800],
]

level_0 = ['영업이익','당기순이익']
level_1 = ['컨센서스','잠정치']
columns = pd.MultiIndex.from_product(
    [level_0,level_1] )

df = DataFrame(data=data, 
    index=['2020/06','2020/09'],
    columns=columns)
print(df.stack())

# 기본적으로 높은 레벨(level)의 컬럼이 인덱스로 
# 변경되지만 level 옵션을 사용해서 특정 컬럼을 
# 인덱스로 변경할 수 있습니다.
print(df.stack(level=0))

# 컬럼이 존재한다면 반복해서 stack 메서드를 
# 호출할 수도 있습니다. 
# 2차원 컬럼을 가진 원본 데이터프레임에 stack 메서드를 
# 두 번 사용하면 모든 컬럼이 인덱스로 이동하고 
# 데이터가 길게 쌓입니다.
print(df.stack().stack())


# 보다 실용적인 예를 살펴봅시다. 
# 그림 의 (a)에는 분기 단위로 자본금과 
# 부채가 정의돼 있습니다. 
# (b)와 같이 연도별 합산된 데이터가 읽기 좋기 때문에 
# (a)를 (b) 형태로 가공하려면 어떻게 연산을 
# 적용해야 할까요? 
# (a)의 2020년도에는 3월, 6월, 9월의 세 컬럼이 
# 존재하며 2021년에는 3월, 6월 두 개의 컬럼으로 
# 월별 데이터가 가변인 것에 주의하세요. 
# 예제에서는 5개의 컬럼을 사용했지만, 
# 실전에서는 수백 개의 컬럼이 존재할 수 있습니다. 
# 데이터를 분석하기 위해서는 컬럼의 연도와 월을 
# 분리해야 하는데, 
# 연도와 월이 컬럼에 위치해서 브로드 캐스팅을 
# 사용하기가 쉽지 않습니다. 
# 이러한 이유로 컬럼을 index로 변경한 뒤에 
# 브로드 캐스팅 기능을 활용해서 연도와 월을 분리해야 합니다. 
# stack을 사용해야겠죠?
data = [
    [1000, 1100, 900, 1200, 1300],
    [800, 2000, 1700, 1500, 1800]
]
index = ['자본금', '부채']
columns = ["2020/03", "2020/06", "2020/09", "2021/03", "2021/06"]
df = DataFrame(data, index, columns)

# stack을 적용해서 컬럼을 2차원 인덱스로 만든 뒤에 
# 인덱스를 다시 값으로 변경하여 
# 그림의 (a)와 같은 데이터프레임으로 만듭니다. 
# 기존의 컬럼과 인덱스의 이름이 존재하지 않았기 때문에, 
# 자동으로 생성된 level_0와 level_1, 0 이름이 
# 부여됐습니다.
df_stacked = df.stack().reset_index() 

# level_1 컬럼을 선택해서 각각의 문자열에 
# split 메서드를 적용합니다. 
# split한 결과 시리즈가 반환되며, 
# 각각의 값이 연도와 월로 분리된 리스트입니다.
temp = df_stacked['level_1'].str.split('/')
print(temp)

# 반환된 시리즈를 리스트로 변환한 다음 데이터프레임 객체로 
# 변환해서 그림의 (b) df_split을 만듭니다.
df_split = DataFrame( list(df_stacked['level_1'].str.split('/')) )

# df_stacked와 df_split 두 개를 합치고 컬럼의 이름을 부여해서 
# 그림의 (c)를 만들 수 있습니다. 
# 이처럼 데이터프레임은 위/아래로 긴 형태로 데이터가 정리돼 있어야 
# 가공하기 쉽기 때문에 stack 메서드를 사용합니다.
df_merged = pd.concat( [df_stacked, df_split], axis=1)
df_merged.columns = ['계정','년월','금액','연도','월']
print(df_merged)

# 계속해서 groupby 메서드를 사용하여 부채와 자본금을 연도별로 정리해 봅시다. 
# 계정과 연도를 기준으로 데이터를 그룹화 (인덱스로 정리)하고 모든 값을 더합니다. 
# 다음과 같이 groupby 메서드에 리스트로 여러 값을 전달하면 멀티 인덱스를 갖는 
# 데이터프레임이 반환됩니다. 
# 코드를 실행한 결과 그림의 (a)와 같이 계정과 연도를 기준으로 금액이 합산됩니다. 
# 그림 (c)의 "년월" 컬럼은 데이터 타입이 object (문자열)이라서 sum() 함수의 호출 결과 
# 자동으로 제거됐습니다.
df_group = df_merged.groupby(["계정","연도"]).sum() 
print(df_group)

# unstack 메서드를 사용해서 그림 (b)와 같이 level 1 인덱스인 
# 연도를 컬럼으로 변경합니다. 
# 이차원 컬럼을 갖는 데이터프레임에서 level 0 컬럼 "금액"을 선택하고, 
# 컬럼과 인덱스의 이름을 제거해서 그림 의 (c) 데이터프레임을 만듭니다.
df_unstack = df_group.unstack()
result = df_unstack['금액']
result.columns.name = ''
result.index.name = ''
print(result)

