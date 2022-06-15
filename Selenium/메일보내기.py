import smtplib
from email.mime.text import MIMEText

#http는 하이퍼텍스트. 이미지, 글자 보내는거. 파일 보내는 거.
#smtp는 .. send mail. 메일 보낼 때 쓰는 거. 
#ehcp ??? 동적 프로토콜? 그중 하나가 smtp ??


smtpName = 'smtp.naver.com' #smtp서버명 넣은 거.
smtpPort = 587

sendEmail = 'narae0609@naver.com'
password= 'ddd'
recvEmail= 'narae0609@naver.com'

title= '제목이다'
content = '내용이다ㅏ아아'

msg= MIMEText(content)  #mimetext 객체 만들어서여기에 내용 담음
msg['From'] = sendEmail
msg['To']= recvEmail
msg['Subject']=title

#메일 발송 '마임 객체에 담ㅇㅏ서 서버연결 -> 로그인 -> 그다음 메일보냄'
s= smtplib.SMTP(smtpName, smtpPort)
#서버주소와 포트를 넣은 거지

s.starttls()
#서버 접근

s.login(sendEmail, password)
s.sendmail(sendEmail, recvEmail, msg.as_string() )
s.close()