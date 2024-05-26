# shareinfo_.py
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# .envファイルから環境変数をロード
load_dotenv()

def send_email(subject, body, to_email):
    from_email = "your_email@example.com"
    from_password = os.getenv('EMAIL_PASSWORD')

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.close()
        return "Email sent successfully!"
    except Exception as e:
        return str(e)

def share(selected_realestates, to_email):
    if selected_realestates and to_email:
        subject = "Selected Real Estates"
        body = "\n".join(selected_realestates)
        result = send_email(subject, body, to_email)
        return result
    else:
        return 'Please select real estates and provide a recipient email!'