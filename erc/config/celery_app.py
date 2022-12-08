import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "send-spam-every-3-hours": {
        'task': 'esn.tasks.updating_debt_task',
        'schedule': crontab(minute='*/3')
    }
}
