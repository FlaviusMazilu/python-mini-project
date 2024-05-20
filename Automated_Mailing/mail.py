from os import getenv
from dotenv import load_dotenv
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()
from_addr='ENTER_SENDERS_MAILID'

data=pd.read_csv("abc.csv")         # Enter path of CSV files containing emails
to_addr=data['email'].tolist()      # Change'email' to column name containg emailids
name = data['name'].tolist()

length=len(name)

for i in range (length):
    msg=MIMEMultipart()
    msg['From']=from_addr
    msg['To']=to_addr[i]
    msg['subject']='Just to Check'

    body=name[i]+'Enter your content here' 

    msg.attach(MIMEText(body,'plain'))

    email= getenv('email')   #Enter Your email id here
    password= getenv('password')     #Enter your Password

    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(email,password)
    text=msg.as_string()
    mail.sendmail(from_addr,to_addr[i],text)
    mail.quit()