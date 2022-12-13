import getpass
import random
import smtplib
import qrcode

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

from django.db.models import F

from esn.models import ObjectModel
from contacts.models import Contacts
from config.celery_app import app


@app.task
def updating_debt_task():
    snippet = ObjectModel.objects.all()
    debt = random.randint(5, 500)
    snippet.update(debt=(F("debt") + debt))
    return "DONE"


@app.task
def reduce_debt_task():
    snippet = ObjectModel.objects.all()
    debt = random.randint(100, 10000)
    for new_debt in snippet:
        if new_debt.debt <=0:
            snippet.update(debt=0)
        else:
            snippet.update(debt=(F("debt") - debt))
    return "DONE"

@app.task
def reset_debt_task(queryset):
    return queryset.update(debt=0)


@app.task
def send_email_task(data):
    qr_code = qrcode.make(data)
    qr_code.save("static/new_img.png")

    queryset = Contacts.objects.all()
    password = getpass.getpass("Enter your password: ")
    for email in queryset:
        reciever = email.email
        sender = "ben300300@gmail.com"

        msg = MIMEMultipart()
        msg['To'] = reciever
        msg['From'] = sender
        msg['Subject'] = "Qr_code"
        msg_ready = MIMEText("Your qr_code: ")
        image = MIMEImage(open("static/new_img.png", 'rb').read(), "png", name="QR_CODE")

        msg.attach(msg_ready)
        msg.attach(image)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as mail:
        mail.login(sender, password)
        print("OK")

        mail.sendmail(sender, reciever, msg.as_string())
    return "DONE"