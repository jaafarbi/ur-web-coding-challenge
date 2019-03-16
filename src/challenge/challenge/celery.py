from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'challenge.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery("challenge", broker="amqp://guest:guest@localhost//")

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
