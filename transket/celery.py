from celery.schedules import crontab
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transket.settings')

app = Celery('transket')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update_crypto_prices_every_5_min': {
        'task': 'crypto_org.tasks.update_crypto_prices',
        'schedule': crontab(minute='*/5'), 
    },
}
