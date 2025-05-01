import smtplib
import ssl
import os

def send_email(message, subject):
    host = "smtp.gmail.com"
    port = 465
    sender = 'cookin32@gmail.com'
    receiver = sender
    password = os.getenv('pythonGmailPass')
    context = ssl.create_default_context()

    message = f"""
    Subject: New {subject} e-mail

    {message}
    """

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)