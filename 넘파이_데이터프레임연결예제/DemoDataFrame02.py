#컬럼/로우 삭제하기
from xml.sax.xmlreader import IncrementalParser
from pandas import DataFrame

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

#삭제하는 drop 메서드를 제공합니다. 
#파라미터 axis=1은 컬럼 삭제를 axis=0은 로우 삭제를 의미합니다.
df_new = df.drop("현재가", axis=1)
print(df)
print(df_new)

#데이터프레임에서 특정 로우를 삭제하기 위해서는 
#drop메서드에 삭제할 로우의 인덱스와 axis를 0으로 설정한다. 
df_new = df.drop("037730", axis=0)
print(df)
print(df_new)

#만약 원본 데이터프레임에서 로우나 컬럼을 바로 
#삭제하고자 한다면 inplace항목에 True
# df.drop("037730", axis=0, inplace=True)
# print(df)

#여러개를 삭재할 경우 리스트형태로 지정
df.drop(["037730","005760"],
        axis=0, inplace=True)
print(df)

#컬럼 레이블 변경
from pandas import DataFrame

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)
print(df.columns)
print(df.index)

#변경할 컬럼의 레이블을 리스트로 정의하고 columns속성에 바인딩한다. 
#이때 변경하려는 컬럼 레이블 개수와 기존에 정의된 레이블의 개수가 동일해야 한다.
#index의 name이라는 변수의 값도 같이 수정해 본다.
df.columns = ['name','close','fluctuation']
df.index.name = 'code'
print(df)

# 데이터프레임 객체의 rename 메서드를 사용하여 컬럼 레이블을 변경할 
# 수도 있다. 
# rename 메서드는 변경하고자 하는 컬럼에 
# {“변경 전 이름”: “변경 후 이름”}과 같은 딕셔너리를 
# 메서드의 인자로 전달한다. 
# 컬럼명 중 일부만을 변경하고자 할 때 유용하게 사용할 수 있다. 
# 'inplace=True'는 원본 데이터프레임을 바로 수정하는 옵션이다.

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)
df.rename(columns={'종목명': 'code'}, inplace=True)
print(df)

#데이터 타입 변경
from pandas import DataFrame

data = [
    ["1,000", "1,100", "1,510"],
    ["1,410", "1,420", "1,790"],
    ["850", "900", "1,185"],
]
columns = ["03/02", "03/03", "03/04"]
df = DataFrame(data=data, columns=columns)
print(df)

#수치 연산을 위해 아래와 같이 변경한다. 
# def remove_comma(x):
#     return int(x.replace(',',''))

# df['03/02'] = df['03/02'].map(remove_comma)
# df['03/03'] = df['03/03'].map(remove_comma)
# df['03/04'] = df['03/04'].map(remove_comma)
# print(df)

#위의 코드는 반복되는 코드로 가독성이 떨어진다.
#판다스의 DataFrame은 전체 데이터에 연산을 적용하는 
#applymap메서드를 제공한다. 
def remove_comma(x):
    return int(x.replace(',',''))

df = df.applymap(remove_comma)
print(df)
print(df.dtypes)


#astype메서드를 사용해도 된다.
import numpy as np
from pandas import DataFrame

def remove_comma(x):    
    return x.replace(",", "")
    
data = [
    ["1,000", "1,100", "1,510"],
    ["1,410", "1,420", "1,790"],
    ["850", "900", "1,185"],
]

columns = ["03/02", "03/03", "03/04"]
df = DataFrame(data=data, columns=columns)
df = df.applymap(remove_comma)
df = df.astype( {"03/02":np.int64, 
                 "03/03":np.int64, "03/04":np.int64} )
print(df.dtypes)


#컬럼의 문자열 다루기
from pandas import DataFrame
import numpy as np

data = [
    {"cd":"A060310", "nm":"3S", "close":"2,920"},
    {"cd":"A095570", "nm":"AJ네트웍스", "close":"6,250"},
    {"cd":"A006840", "nm":"AK홀딩스", "close":"29,700"},
    {"cd":"A054620", "nm":"APS홀딩스", "close":"19,400"}
]
df = DataFrame(data=data)
print(df)

#다앙한 전처리를 위한 메서드를 제공한다.
#cd컬럼의 종목코드에서 A를 제거한 후 나머지 6자리를 사용하도록 변경한다. 
df['cd'] = df['cd'].str[1:]
print(df)

#이번에는 'close'컬럼에 대해서 컴마를 제거해본다. 
df['close'] = df['close'].str.replace(',', '').astype(np.int64)
print(df)