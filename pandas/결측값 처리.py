import pandas as pd
import numpy as np

df= pd.read_excel('score.xlsx', index_col = '지원 번호')

print(df.fillna(''))   #nan을 빈공백처리해서 출력
print(df.fillna('없음')) #nan값에 없음을 넣어서 출력.
#fillna 안에 inplace=True넣으면 데이터 자체를 바꿔줌.

print(df.dropna())   #결측값이 있는 row를 없애버림. 이것도 데이터 자체에 영향 주려면 inplace=True 넣고.
print(df.dropna(axis='index'))  #결측값이 있는 row 삭제. 해당 index 삭제. 위와 같음.
print(df.dropna(axis='columns'))  #결측값이 있는 column을 삭제.
print(df.dropna(axis='columns', how='any')) #how= 'any', 한개라도 있으면. 'all', 전체 결측값이면.


# df['학교']= np.nan  #해당컬럼의 값 치환. 
# print(df)