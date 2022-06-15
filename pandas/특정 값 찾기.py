import pandas as pd
df= pd.read_excel('score.xlsx', index_col = '지원 번호')

print(df.loc[['1번','3번'],['이름','키']])   #인덱스와 컬럼을 한번에 지정해서 출력 가능, 여러개 말할 때는 꺾쇠 넣어서 리스트로 만들고.
print(df.loc['1번':'5번', ['이름','키']])      #범위로 할때는 리스트가 아니니까 꺾쇠를 추가 안해도 됨


print(df.iloc[[3,5], 2])    #index 3,5번의 2번째 컬럼에 해당하는 값들 출력.
print(df.iloc[0:5, 3:6])  #이건 꺾쇠 안에 딕셔너리니까 추가적 꺾쇠 넣을 필요가 없음


