import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

gmail_user = os.getenv('GMAIL_USER')
gmail_password = os.getenv('GMAIL_PASSWORD')


def send_email(header, body, recipient_email):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Port 587 is used for TLS encryption
        server.starttls()  # Enable TLS (Transport Layer Security)
        server.login(gmail_user, gmail_password)
    except Exception as e:
        print("Error: Unable to connect to Gmail's SMTP server.")
        print(e)
        exit()
    
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = recipient_email
    msg['Subject'] = header
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server.sendmail(gmail_user, recipient_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Error: Unable to send email.")
        print(e)
    
    server.quit()
