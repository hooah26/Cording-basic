import pandas as pd
df = pd.read_excel('coding-basic/score.xlsx')

df['SW특기']= df['SW특기'].str.lower() # 컬럼의 데이터 수정
df['학교'] = df['학교']+'등학교'   #컬럼값 변경

# 컬럼 추가
df['총합'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
print(df)

#직접 컬럼값 입력 통한 컬럼 추가
df['학년']=[3,3,2,1,1,3,2,2]

#모든 row의 컬럼값 동일한 컬럼 추가
df['결과'] = 'pass'



filterdata = df['총합'] >= 400
df.loc[filterdata, '결과'] = 'Pass'  # filterdata가 참인 row들의, 결과 컬럼값에 pass를 넣는다.'

#특정 인덱스 특정 컬럼의 값 수정
df.loc['4번', '학교'] = '왕왕고'

#특정 컬럼 삭제
df.drop(columns=['국어','영어','수학'], inplace=True)

#값 수정
df.replace({'구로고':'영등포고'}, inplace=True)

#컬럼명 수정
df.rename(columns={'이름':'name', '학교':'school'}, inplace=True)

#컬럼명 일괄수정
# df.columns=['name', 'school',...] 개수맞춰서