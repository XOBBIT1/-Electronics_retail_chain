import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "update-debt-every-2-minutes": {
        "task": "esn.tasks.updating_debt_task",
        "schedule": crontab(minute="*/2"),
    },
    "reduce-debt-every-2-minutes": {
        "task": "esn.tasks.reduce_debt_task",
        "schedule": crontab(hour="6", minute="30"),
    },
}
