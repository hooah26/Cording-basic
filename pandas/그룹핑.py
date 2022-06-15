import pandas as pd
df= pd.read_excel('score.xlsx', index_col='지원 번호')

df.groupby('학교').get_group('구로고') #학교별로 그룹 나누고 그 그룹 중에 구로고를 뽑아라

df.groupby('학교')['키'].mean()   #학교별로 그룹 나눠서 키 컬럼의 평균 구하기
df.groupby('학교')['키'].size()   #학교별로 그룹 나눠서 키 컬럼의 개수 구하기
df.groupby('학교')['키'].size()['구로고']   #학교로 나눠서 키의 개수를 보는데 그중 구로고의 것을 본다.
df.groupby('학년').mean().sort_values('키')   #학년으로 그룹 나눠서 계산 가능한 컬럼별 평균을 출력하는데, 그걸 '키'의 값으로 정렬한다. 역순으로 하려면 ascending=False.


df.groupby(['학교','학년']).sum()   # 학교로 1차 분류, 학년으로 2차 분류한 뒤 분류한 것 별로 컬럼의 sum 출력한다.
df.groupby(['학교','학년']).mean()  #1차 학교 2차 학년으로 분류하고 각 컬럼별 평균값을 출력한다.
df.groupby('학교')['이름'].count() #학교로 그룹핑한후, 그룹마다 이름 컬럼의 값이 몇개 있는지를 출력한다. (결측치 뺀 컬럼값 개수 확인할 수 있는 것.)
df.groupby('학교')['이름','sw특기'].count()    #학교로 그룹핑한 후 그 중 이름과 sw특기 값을 카운트

print(df.groupby('학교')['키'].value_counts() )  #학교로 그룹나눠서  키 컬럼값마다의 개수.
print(df.groupby('학교')['학년'].value_counts())    #학교로 그룹 나눠서 학년 컬럼값마다의 개수.
