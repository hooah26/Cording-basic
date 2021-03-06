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

df= pd.DataFrame(data, columns=['이름', '학교', '키'])   #데이터 중 원하는 컬럼만 가져와서 dataframe (2차원 배열) 객체를 만들 수도 있다.
df = pd.DataFrame(data, columns=['이름','국어','영어','수학','학교','키'])  #컬럼 순서를 변경할 수 있다
df= pd.DataFrame(data, index=['1번','2번','3번','4번','5번','6번','7번','8번']) # 인덱스 설정


df.index.name = '번호'  #index의 이름 지정. 인덱스의 컬럼 이름.
df= pd.DataFrame(data, index=['1번','2번','3번','4번','5번','6번','7번','8번'], columns=['이름','국어', '키'])   
#인덱스 설정하고, 컬럼 지정.


df.reset_index(inplace=True) #인덱스 리셋해서 생성 근데 이러면 기존에 설정된 인덱스 컬럼이 일반 컬럼으로 남아있음
df.reset_index(drop=True, inplace=True) #이렇게 해야 인덱스로 설정되어 있는 컬럼이 삭제.
df.set_index('키', inplace=True) #기존에 있는 컬럼 중 키 컬럼을 인덱스로 지정


df.sort_index(ascending=False, inplace=True)
print(df)
