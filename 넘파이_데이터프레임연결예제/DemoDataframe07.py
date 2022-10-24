#Pivot
# 엑셀에서 피벗 (Pivot)은 필요한 데이터를 추출해서 데이터를 
# 재구성하는 기능을 일컫습니다. 
# 이와 유사하게 데이터프레임의 피벗 기능 또한 인덱스와 컬럼 및 
# 데이터를 지정해서 새로운 데이터프레임을 생성합니다. 
# 피벗을 사용하여 데이터를 재구조화함으로써 데이터를 다양한 측면에서 
# 분석할 수 있게 됩니다. 
# 우선, 피벗에 사용할 데이터프레임을 정의해 봅시다.
from pandas import DataFrame
import pandas as pd

data = [
    ["2021-08-12", "삼성전자", 77000],
    ["2021-08-13", "삼성전자", 74400],
    ["2021-08-12", "LG전자", 153000],
    ["2021-08-13", "LG전자", 150500],
    ["2021-08-12", "SK하이닉스", 100500],
    ["2021-08-13", "SK하이닉스", 101500]
]
columns = ["날짜", "종목명", "종가"]
df = DataFrame(data=data, columns=columns)
print(df)

# 판다스의 pivot 함수는 data, index, columns, values 파라미터를 입력받습니다. 
# data에는 피벗할 원본 데이터프레임을 연결하며, 
# 나머지 파라미터는 이름이 직관적이라 추가 설명이 필요 없겠죠? 
# 다음 코드의 실행 결과를 보고 피벗이 어떻게 동작하는지 이해해 봅시다.
df = pd.pivot(data=df, index='날짜', columns='종목명',
    values='종가')
print(df)

# groupby와 unstack을 사용해서 그림과 같은 결과를 
# 만들 수도 있습니다. 
# 날짜와 종목명 컬럼으로 그룹화한 다음 level 1 인덱스인 
# 종목명을 컬럼으로 변경하도록 unstack 메서드를 적용합니다. 
# 한 번에 이해 가지 않는다면 단계별로 결과를 확인해서 
# 동작 과정을 확인해 보세요.
print( df.groupby(['날짜','종목명']).mean().unstack() )

# 이번에는 인덱스로 종목명, 컬럼으로 날짜, 데이터로 종가를 
# 지정해 보겠습니다.
# df = pd.pivot(data=df, index="종목명",
#             columns="날짜", values="종가")
# print(df)


#Melt
# 데이터프레임의 melt 메서드는 컬럼의 수가 많아서 
# 넓은 와이드 포맷의 데이터프레임을 세로로 긴 롱 포맷의 
# 데이터프레임으로 재구조화합니다. 
# 영어 단어 melt는 '녹이다'라는 뜻이 있으며, 
# 데이터프레임에서는 '컬럼을 녹여 값으로 변경한다' 정도로 이해할 수 있습니다. 
# melt를 실습할 데이터프레임을 정의해 봅시다
from pandas import DataFrame

data = [
    ["005930", "삼성전자", 75800, 76000, 74100, 74400],
    ["035720", "카카오", 147500, 147500, 144500, 146000],
    ["000660", "SK하이닉스", 99600, 101500, 98900, 101500]
]

columns = ["종목코드", "종목명", "시가", "고가", "저가", "종가"]
df = DataFrame(data=data, columns=columns)
print(df)

# 모든 값이 value로 변경되니 가독성이 떨어집니다. 
# id_vars 파라미터를 사용해서 melt하지 않을 컬럼의 이름을 리스트로 지정할 수 있습니다. 
# 다음은 종목명과 종목코드 제외하고 나머지 데이터를 melt합니다.
print(df.melt(id_vars=['종목코드','종목명']))

# 위의 결과는 id_vars를 사용한 melt 메서드로 얻은 데이터프레임의 일부입니다. 
# 종목코드와 종목명 컬럼은 그대로 유지되었고 나머지는 variable과 value 컬럼으로 
# 변경되었습니다.

# 특정 컬럼을 슬라이싱한 뒤에 melt 메서드를 적용할 수도 있습니다. 
# 리스트로 컬럼 슬라이싱 후 melt를 적용할 수 있지만, 
# 이번에는 melt의 value_vars 파라미터를 사용해 보겠습니다. 
# id_vars와 유사하게 리스트로 컬럼의 이름을 전달합니다.
print( df.melt(value_vars=['시가','종가']) ) 

#파일 저장하기
# 판다스의 데이터프레임 객체는 여러 포맷으로 저장할 수 있습니다. 
# 예를 들어 to_csv 메서드를 사용하면 CSV 파일로 저장할 수 있고 
# to_excel 메서드를 사용하면 엑셀 파일로 저장할 수 있습니다. 
# 데이터베이스로 저장하는 to_sql, 
# 웹페이지로 표현할 수 있는 to_html 등의 다양한 메서드가 있지만, 
# 원리는 비슷해서 이번 절에서는 데이터프레임을 CSV 파일과 엑셀 파일로 
# 저장하는 방법을 알아보겠습니다. 연습에 사용할 데이터프레임을 정의해 봅시다.
from pandas import DataFrame

data = {
    "종목코드":["037730", "036360", "005760"],
    "종목명": ["3R", "3SOFT", "ACTS"],
    "현재가": [1510, 1790, 1185],
    "등락률": [7.36, 1.65, 1.28],
}

#columns = ["종목코드","종목명","현재가","등락률"]
df = DataFrame(data) 

#파일로 저장
df.to_csv("data.csv")

#엑셀로 저장
df.to_excel("data.xlsx")

#시트이름을 지정하는 경우
df.to_excel("data2.xlsx", sheet_name="종목정보")

#인덱스를 제외할 경우
df.to_excel("data3.xlsx", index=False)

#컬럼명을 생략할 경우
df.to_excel("data4.xlsx", header=False)



#파일 읽기
# 엑셀 파일을 읽을 때 엑셀 파일의 특정 컬럼을 데이터프레임의 인덱스로 지정할 수 있습니다. 
# index_col 파라미터에 인덱스로 사용할 컬럼의 이름을 전달합니다.
df = pd.read_excel("code.xlsx", index_col='cd')
print(df)

# 컬럼의 이름 "cd" 대신 숫자 인덱스로 데이터프레임의 인덱스를 
# 지정할 수 있습니다. 인덱스는 왼쪽 끝에서부터 0으로 시작하며 순차 증가합니다.
# 'cd'는 1번 위치에 있어서 다음 코드와 같이 index_col=1이라고 지정하면 
# 그림과 같은 결과를 반환합니다.
df = pd.read_excel("code.xlsx", index_col=1)
print(df)

# 얻어온 데이터프레임에는 불필요한 'Unnamed: 0' 이름의 컬럼이 존재합니다. 
# 엑셀 파일을 읽을 때 해당 컬럼을 제거하고 데이터프레임 객체로 읽어 보겠습니다. 
# 이를 위해 usecols 파라미터를 사용합니다. usecols은 인덱스를 0부터 
# 사용하므로 usecols=[1, 2, 3]은 두 번째, 세 번째, 네 번째 컬럼만을 
# 사용함을 뜻합니다.
df = pd.read_excel("code.xlsx", index_col='cd', usecols=[1,2,3])
print(df)

# 특정 행 이후부터 엑셀을 읽으려면 header 파라미터를 사용합니다. 
# 다음 코드의 header=2는 2번 행부터 데이터를 읽으라는 의미입니다. 
# 인덱스는 0부터 시작하기 때문에 세 번째 행부터 읽어오겠죠?
# df = pd.read_excel("code2.xlsx", header=2, index_col='cd', usecols=[1, 2, 3])


# CSV 파일은 read_csv 함수를 사용합니다. 
# read_excel 함수와 유사하게 header, index_col, usecols 옵션을 
# 모두 사용할 수 있습니다. 
# 다음은 주피터 노트북과 같은 경로에 존재하는 maginc.csv 파일을 읽습니다.
df = pd.read_csv("magic.csv")
print(df)

# CSV 파일을 판다스로 읽을 때 그림의 종목코드 컬럼과 같이 앞쪽에 위치하는 0이 
# 사라지는 문제가 종종 발생합니다. 
# read_csv 함수는 각 컬럼의 데이터 타입을 추정하는데, code 컬럼이 숫자라고 
# 판단돼서 001800이 정수 1800으로 출력됩니다. 
# 데이터프레임의 dtypes 속성을 출력해서 데이터 타입을 확인해 보세요.
df = pd.read_csv("magic.csv", dtype={'code':str})
print(df)
