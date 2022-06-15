import pandas as pd

data = {
'이름' : ['강나래', '강태원', '강호림', '김수찬', '김재욱', '박동현', '박혜정', '승근열'],
'학교' : ['구로고', '구로고', '구로고', '구로고', '구로고', '디지털고', '디지털고', '디지털고'],
'키' : [197, 184, 168, 187, 188, 202, 188, 190],
'국어' : [90, 40, 80, 40, 15, 80, 55, 100],
'영어' : [85, 35, 75, 60, 20, 100, 65, 85],
'수학' : [100, 50, 70, 70, 10, 95, 45, 90],
'과학' : [95, 55, 80, 75, 35, 85, 40, 95],
'사회' : [85, 25, 75, 80, 10, 80, 35, 95],
'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

df=pd.DataFrame(data)
# df=pd.DataFrame(data, index=['1번','2번','3번','4번','5번','6번','7번','8번'])
# df.index.name='지원 번호'
# print(df)
# print(df['이름'])   #이거는 컬럼.
#1차원 시리즈에서 됐던 건 그 인덱스가 컬럼의 기능이어서 그랬음.. 컬럼이 가능함.

# print(df.loc[0])   #이게 row기준.
# print(df[0:3])   #이런식으로 row 범위 지정해서 뽑아올 수도 있다.
# print(df[3:4])  #인덱스 범위   3에서 시작, 4 이전까지 즉 3 한 개만 나옴. 위에 콜롬값 나오고.  이건 0부터 세고
print(df.loc[3:4])   #이러면 인덱스 3번이 나옴! 이게 더 직관적..


df= pd.read_excel('score.xlsx', index_col='지원 번호')

print(df[3:4])  #인덱스 범위   3에서 시작, 4 이전까지 즉 3 한 개만 나옴. 위에 콜롬값 나오고.
print(df['국어'].nlargest(3))   #해당 컬럼의 값이 큰 순서로 row 3개 보여줌    
print(df['국어'].nsmallest(3))
print(df['학교'].unique())    #해당 컬럼의 값 중복없이 보여줌

print(df.columns[0])   #0번째 컬럼값의 이름을 가져옴.
print(df.columns[-1])   #마지막 컬럼값의 이름
print(df[df.columns[0]])   #0번째 컬럼값의 이름을 df[] 안에, 즉 컬럼인덱스로 넣은 거니까 그 컬럼에 해당하는 값들을 보여줌

print(df.loc['3번'])  #설정한 인덱스컬럼의 값으로 찾는 것. 지원번호를 인덱스 컬럼으로 해놨으니 '3번'을 넣어야함.
print(df.iloc[3])  #이건 인덱스로케이션이라서 0부터 시작함
print(df.iloc[0])  #이러면 0 인덱스.. 1번 학생이 나옴




df= pd.read_excel('월간.xlsx',   skiprows=3, index_col='행정기관', usecols='B, E:O') 
#usecols='B:E'    usecols='B,E:O' 이런식으로 몇 컬럼만 들고올 수 있음. / 부른 이후 인덱스 컬럼 설정할거면 df.set_index('행정기관', inplace=True).


print(df.index.values)
print(df.loc['부산광역시  '])   #인덱스 컬럼 값이 부산광역시인 row 보여줌

df.rename(index={'부산광역시  ':'부산광역시'}, inplace=True)   #인덱스값 변경. 컬럼스 값 변경도 같은 방식.





df.iloc[0] = df.iloc[0].str.replace(',','').astype(int)   #쉼표를 바꾸고, 타입은 int로 바꿈
