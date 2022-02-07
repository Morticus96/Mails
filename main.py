import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time

MY_ADDRESS = "example@gmail.com"
MY_PASSWORD = "haslo maslo"

HOST_ADDRESS = 'smtp.gmail.com'
HOST_PORT = 587

server = smtplib.SMTP(host=HOST_ADDRESS, port=HOST_PORT)
server.starttls()
server.login(MY_ADDRESS, MY_PASSWORD)

plik = open('maile.txt')

for linia in plik:
    RECIPIENT_ADDRESS = linia.strip()
    message = MIMEMultipart()

    message['From'] = MY_ADDRESS
    message['To'] = RECIPIENT_ADDRESS
    message['Subject'] = "Przykladowy Tyrol"


    # HTML Setup
    html = """<html>
    <head></head>
        <body>
         <p><img src="https://miro.medium.com/max/601/1*H8TK1BK5H12X65M8OL0nUQ.png" alt="The Bloomer: A Meme that Society Should Strive to Be | by Michael Roy |  Medium" /></p>
         <h2 style="text-align: center;"><strong>Let There Be Bloomer meine leutnant!</strong></h2>
         <p>Lorem ipsum went on vacation and ate all cookies, its not bad he is just lonley. But he met Cap. Prince and Sgt. Reznov, and they conquered enemy fortress without hesetation. Glorry Glorry Hallelujah!&nbsp;</p>
         <p>Now, alors on danse!</p>
        </body>
    </html>"""

    htmlPart = MIMEText(html, 'html')

    filename = "document.txt"
    filePart = MIMEApplication(open(filename,"rb").read(),Name=filename)
    filePart["Content-Disposition"] = 'attachment; filename="%s' % filename

    filename1 = "document1.txt"
    filePart1 = MIMEApplication(open(filename1,"rb").read(),Name=filename1)
    filePart1["Content-Disposition"] = 'attachment; filename="%s' % filename1

    filename2 = "document2.txt"
    filePart2 = MIMEApplication(open(filename2,"rb").read(),Name=filename2)
    filePart2["Content-Disposition"] = 'attachment; filename="%s' % filename2

    filename3 = "lorem ipsum.txt"
    filePart3 = MIMEApplication(open(filename3,"rb").read(),Name=filename3)
    filePart3["Content-Disposition"] = 'attachment; filename="%s' % filename3

    message.attach(htmlPart)
    message.attach(filePart)
    message.attach(filePart1)
    message.attach(filePart2)
    message.attach(filePart3)

    server.send_message(message)
    print("Sending massage to: ", RECIPIENT_ADDRESS )
    time.sleep(3)
server.quit()
