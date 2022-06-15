import pandas as pd
df= pd.read_excel('score.xlsx', index_col='지원 번호')

print(df['키']>=185)  # row마다 해당 컬럼이 조건 만족하는지 불린타입으로 나옴
a= df['키']>=185

print(df[a])   #a 해당 조건을 만족하는, 해당 조건이 참인 row가 나옴
print(df[~a])



# and  & ,  or |
print(df[(df['키']>=185) & (df['학교']=='구로고')  ])
# df[ 조건a  &  조건b]



filter= (df['영어']>=90) & (df['수학']>=90) & (df['이름'].str.contains('ch'))
print(df.loc[filter])


fdata= df['sw특기'].str.contains('Java', na=False)   #넌값 NaN 포함할건지 제외할건지를 명시해줘야함
#str.contains에서 대소문자 구분할 거면 case=True, 대소문자 구분 없을 거면 case=False.

langs=['python']
swfilter=df['sw특기'].str.lower().isin(langs)        #isin으로 리스트 내의 값을 포함하는가의 조건으로 찾을 수 있음.
namefilter= df['이름'].str.contains('to')  #df의 '이름'컬럼 값들이 해당 조건을 만족하는지를 불린으로 뽑음.
print(df[namefilter])
print(namefilter)  #불린데이터

print(df[swfilter   & namefilter] )   #두가지 조건 모두 참인 row를 찾는다.


filterdata= df['이름'].str.startswith('강')
print(df[filterdata])