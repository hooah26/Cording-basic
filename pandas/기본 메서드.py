import pandas as pd
df= pd.read_excel('score.xlsx', index_col='지원 번호')
# df= pd.read_excel('score.xlsx')
# print(df)


# print(df.describe())   #수치상으로 계산 가능한 컬럼에 대해서 나옴
# print(df.info())  #컬럼의 정보 출력
# print(df.head()) #기본적으로 5개만 출력, 안에 값 넣을 수도 있음
# print(df.tail())
# print(df.values)   #값만 가져옴.
# print(df.index )
# print(df.columns)

print(df.shape)