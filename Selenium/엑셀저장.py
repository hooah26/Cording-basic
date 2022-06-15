import csv
import requests
from bs4 import BeautifulSoup


# 웹스크래핑 기본형태
url='https://finance.naver.com/sise/sise_market_sum.naver?&page=1'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers=headers)   #url의 정보 requests로 가져온 객체 res.
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")   #url 정보 가져온 객체인 res의 text속성을 lxml로 파싱해주는 beautifulsoup과, lxml로 파싱한 객체인 soup.

# 파일이름 선언
filename="시가총액_20220216.csv"
 
#파일 객체 열며 생성하고
f = open(filename,"w",encoding="utf-8-sig",newline="")

#csv형식으로 적겠다.
mycsvfile = csv.writer(f)

title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t") #리스트 만든 것.
mycsvfile.writerow(title) # 한 줄에 리스트 넣음.  writerow로 저장을 하려면 list형태로 저장이 되어야 함.


data_rows = soup.find("table",{"class":"type_2"}).find("tbody").find_all("tr")
# data_rows = soup.find(class_='type_2')  # class를 찾는 단축형태
# print(soup.prettify())  # html소스가 정렬이 되어서 출력이 됨

for row in data_rows:
    columns = row.find_all("td")   #find_all이니까 리스트 형태.
    # td가 1개만 있을때는 내용이 없으므로 제외
    if len(columns) <= 1:
        continue   #스킵하고 다음 row 포문으로 가라는 거.
    #즉 td가 여러개로 이루어진, 우리가 찾고자 하는 row일 때만 아래 실행.

    # data = [column.get_text().strip() for column in columns ]   한줄포문 []로 감싸면, 결과가 리스트로 저장됨.
    data=[]
    for column in columns:
        data.append(column.get_text().strip())    #아니면 이렇게 미리 data를 리스트 형식으로 해놓고 어펜드 해도 되고.
    mycsvfile.writerow(data)   #하나의 row마다 하나의 리스트데이터 있고 그거를 한 줄씩 writer객체에 적어라.