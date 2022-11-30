from celery import shared_task
import random

from django.db.models import F

from esn.models import ObjectModel
from erc.celery import app


@app.task
def updating_debt_task():
    print("hello")
    increase_debt = random.randint(5, 500)
    sum_debt = ObjectModel.objects.all().aggregate((F('debt') + increase_debt))
    new_debt = ObjectModel.objects.all().update(debt=sum_debt)
    new_debt.save()

