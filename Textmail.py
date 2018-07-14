import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
 
fromaddr = "keerthana.r@tringapps.com"
toaddr = "martha@tact.ai"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Base64 email conversion"
 
body = "Hello Martha"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, sys.argv[1])
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print("Mail Sent Successfully")
server.quit()
