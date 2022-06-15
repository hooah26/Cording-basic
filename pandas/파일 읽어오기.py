import pandas as pd
# data = {
# '이름' : ['강나래', '강태원', '강호림', '김수찬', '김재욱', '박동현', '박혜정', '승근열'],
# '학교' : ['구로고', '구로고', '구로고', '구로고', '구로고', '디지털고', '디지털고', '디지털고'],
# '키' : [197, 184, 168, 187, 188, 202, 188, 190],
# '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
# '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
# '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
# '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
# '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
# 'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
# }

# df=pd.DataFrame(data, index= ['1번','2번','3번','4번','5번','6번','7번','8번'])
# df.index.name='지원 번호'


# df= pd.read_csv('score.csv', skiprows=[0,5])   #row를 0번, 5번 지우겠다. 그런데 맨 위의 row는 자동으로 컬럼값으로 들어감.
#skiprows = 리스트가 아니라 수 하나를 입력하면, 그 개수의 row를 지우고 가져오겠다는 것.
# df.set_index('지원 번호', inplace=True)   #특정 컬럼을 인덱스로 지정
# print(df)

# df= pd.read_csv('score.csv', skiprows=[3], nrows=3)    #norws 몇개 뽑을 건지
# print(df)

# df= pd.read_csv('score.txt', sep='\t')    #csv는 눌러보면 텍스트로 열리잖아. 메모장으로 연결해서 열 수 있잖아. 더 넓은 듯. csv는 엑셀이 아니라 텍스트야
#                             #엑셀이 csv도 지원하는 거지
# print(df)


# df= pd.read_excel('score.xlsx')
# df.set_index('지원 번호', inplace=True)
# print(df)


df = pd.read_excel('score.xlsx', index_col= '지원 번호')   #파일 불러오며 객체 생성시 인덱스컬럼을 설정할 수 있다
print(df)