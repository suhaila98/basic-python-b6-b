import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sender(recipients): 

    body = 'ISI EMAIL'
    msg = MIMEMultipart()

    msg['Subject'] = 'Test Kirim Email'
    msg['From'] = 'aylaachmad50@gmail.com'
    msg['To'] = (', ').join(recipients.split(','))

    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('aylaachmad50@gmail.com', 'suhaila1998')
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    sender('suhaila2008@gmail.com,hunaifa17@gmail.com')