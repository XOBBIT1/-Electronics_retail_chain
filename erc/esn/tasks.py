from celery import shared_task
from erc.celery import app
from esn.celery_script.celery_script import updating_debt


@shared_task
def updating_debt():
    updating_debt().delay(5)
