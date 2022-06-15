import pandas as pd
df= pd.read_excel('score.xlsx', index_col = '지원 번호')

print(df.sort_values('키'))  #역순정렬은 ascending=False
print(df)

print(df.sort_values(['영어','수학']))
print(df.sort_values(['영어','수학'], ascending=[True, False])) #영어는 순차, 수학은 역순으로

print(df.sort_index(ascending=False)) #인덱스로 역순정렬