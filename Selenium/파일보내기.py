import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#multipart? 폼에있는 데이터를 파일 첨부할 수 있는 형태로 하겠다..??

from email.mime.base import MIMEBase
from email import encoders

#아래 세줄이 파일 첨부하기 위한 거다.

smtpName = 'smtp.naver.com'
smtpPort= 587
sendEmail = 'narae0609@naver.com'
password= 'dd'
recvEmail= 'narae0609@naver.com'

title= '파이썬 파일 첨부'
content = '파일을 첨부해보자 '

msg = MIMEMultipart('alternative')
#아깐 마임텍스트였는데 이번엔 마임멀티팟으로 객체만듦

part2=MIMEText(content)   #텍스트는 따로빼서 어태치로 넣음
msg.attach(part2)
msg['From'] = sendEmail
msg['To']= recvEmail
msg['Subject']=title
#얘네를 다 mime에 넣어서 보낸다 ??


part= MIMEBase('application', 'octet-stream')
with open('시가총액_20220216.csv', 'rb') as f:
    part.set_payload(f.read())
    #마임베이스 객체인 part에다가 파일 읽은 걸 담았다..

encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename='시가총액_20220216.csv')

msg.attach(part)

s= smtplib.SMTP(smtpName, smtpPort)
#서버주소와 포트를 넣은 거지

s.starttls()
#서버 접근

s.login(sendEmail, password)
s.sendmail(sendEmail, recvEmail, msg.as_string() )
s.close()