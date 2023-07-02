#자동적으로 메일을 보내는 프로그램

#
import smtplib
from email.mime.text import MIMEText


smtp_email = 'smtp.naver.com'
smtp_port = 587
s = smtplib.SMTP(smtp_email, smtp_port)
s.starttls()

email = '이메일주소'
email_pw = '비밀번호'

s.login(email,email_pw)

subject = '메가스터디 수업종료'
text = '''하이 가서 쉬고 다음주에 만나욧'''

msg = MIMEText(text)
msg['Subject'] = subject
msg['From'] = email
msg['To'] = '받는 사람 이메일주소'

s.sendmail(email, '받는 사람 이메일 주소', msg.as_string())
s.quit()




