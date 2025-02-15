import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_management.settings')

app = Celery('crypto_management')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Schedule the crypto price update task to run every 5 minutes
app.conf.beat_schedule = {
    'fetch-crypto-prices': {
        'task': 'crypto_data.tasks.fetch_crypto_prices',
        'schedule': 300.0,  # 5 minutes
    },
}