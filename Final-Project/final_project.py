pwd = "******"

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

f =  open('emails.txt','r')
email = f.readlines()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("aylaachmad50@gmail.com",pwd)

body = "Foto pantai terlampir dibawah ya"
sender = "aylaachmad50@gmail.com"

msg = MIMEMultipart()
with open('pantai.jpg', 'rb') as image_file:
    msg.attach(MIMEImage(image_file.read()))
msg.attach(MIMEText(body))
msg['Subject'] = 'Test Kirim Email'
msg['From'] = 'aylaachmad50@gmail.com'
msg['To'] = (', ').join(email)

try:
   server.sendmail(sender, email, msg.as_string())
   print('Message Sent Succesfully')
except:
   print('There Was An Error While Sending The Message')
server.quit()


#Source : https://stackoverflow.com/questions/8856117/how-to-send-email-to-multiple-recipients-using-python-smtplib
#https://answer-id.com/id/53557096
#https://qastack.id/programming/8856117/how-to-send-email-to-multiple-recipients-using-python-smtplib
#https://stackoverflow.com/questions/26630069/python-smtplib-and-mimetext-adding-an-attachment-to-an-email