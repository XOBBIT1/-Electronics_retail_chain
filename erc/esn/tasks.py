import random
import qrcode

from django.db.models import F

from esn.models import ObjectModel
from contacts.models import Contacts
from config.celery_app import app
from esn.email import email


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
        if new_debt.debt <= 0:
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
    email(queryset)
