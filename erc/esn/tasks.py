from celery import shared_task
import random

from django.db.models import F

from esn.models import ObjectModel
from config.celery_app import app


@app.task
def updating_debt_task():
    snippet = ObjectModel.objects.all()
    snippet.debt = random.randint(5, 500)
    return

