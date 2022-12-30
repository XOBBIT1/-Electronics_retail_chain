import smtplib
import getpass

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


def email(queryset):

    password = getpass.getpass("Enter your password: ")

    for email in queryset:
        reciever = email.email
        sender = "ben300300@gmail.com"

        msg = MIMEMultipart()
        msg["To"] = reciever
        msg["From"] = sender
        msg["Subject"] = "Qr_code"
        msg_ready = MIMEText("Your qr_code: ")
        image = MIMEImage(
            open("static/new_img.png", "rb").read(), "png", name="QR_CODE"
        )

        msg.attach(msg_ready)
        msg.attach(image)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as mail:
        mail.login(sender, password)
        print("OK")

        mail.sendmail(sender, reciever, msg.as_string())
    return "DONE"
