import os
from celery import Celery

# назначание переменной окружения с настройками проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_apple_store.settings')

app = Celery('my_apple_store')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()