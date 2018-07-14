import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
fromaddr = "keerthana.r@tringapps.com"
toaddr = "martha@tact.ai"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Howdy!"
 
body = "How are you"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "IMG_C2E1B5A7D294-1.jpeg"
attachment = open("/Users/keerthana/Downloads/IMG_C2E1B5A7D294-1.jpeg", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, sys.argv[1])
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
