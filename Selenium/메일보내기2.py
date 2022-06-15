import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


browser = webdriver.Chrome(options=options)
browser.maximize_window() # 윈도우 창 최대화
url ='https://land.naver.com/'
browser.get(url)  #url 이동

browser.find_element_by_xpath('//*[@id="queryInputHeader"]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="queryInputHeader"]').send_keys('신대방 우성 아파트')
time.sleep(2)
browser.find_element_by_xpath('//*[@id="queryInputHeader"]').send_keys(Keys.ENTER)
time.sleep(4)
browser.find_element_by_xpath('//*[@id="ct"]/div[2]/div[1]/div[2]/div/div/div[2]/div/a/div[1]').click()
time.sleep(4)


page_source= browser.page_source
soup= BeautifulSoup(page_source, 'lxml')

name= soup.find('h3',{'id':'complexTitle'}).get_text()
# price= soup.find('div',{'id':'summaryInfo'}).find('div',{'class':'data'}).get_text()

# //*[@id="summaryInfo"]/div[2]/div[1]/dl/dd[1]
data=[name]



f= open('우성아파트.csv', 'w', encoding='utf-8-sig')
myfile=csv.writer(f)
myfile.writerow(data)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtpName = "smtp.naver.com"
smtpPort = 587
sendEmail = "narae0609@naver.com"
password = "snxpfcjfals"
recvEmail = "narae0609@naver.com"

title = "파이썬 파일 첨부"
content = "파이썬 이메일 파일 첨부 소스 코드입니다."

msg = MIMEMultipart('alternative')
# msg = MIMEText(content)
# 내용부분
part2 = MIMEText(content)
msg.attach(part2)
msg['From'] = sendEmail
msg['To'] = recvEmail
msg['Subject'] = title

# 파일첨부
part = MIMEBase('application',"octet-stream")
# 파일 읽어오기
with open("우성아파트.csv","rb") as f:
    # part에 담기
    part.set_payload(f.read())
# 파일 첨부할수 있는 형태로 인코딩
encoders.encode_base64(part) 
# header정보 정의
part.add_header('Content-Disposition','attachment',filename="파일명 바꿔서 보내볼게요.csv")

msg.attach(part)

# 메일 서버 정보 smtp.naver.com/587
s = smtplib.SMTP(smtpName , smtpPort)         
# 메일 서버 접근
s.starttls()    
# 메일 서버 로그인                            
s.login(sendEmail , password)   
# 메일 발송              
s.sendmail(sendEmail, recvEmail, msg.as_string()) 
# 메일 닫기
s.close()  