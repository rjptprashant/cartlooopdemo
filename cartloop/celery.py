import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cartloop.settings')

celery_app = Celery('cartloop')
celery_app.config_from_object(
    'django.conf:settings',
    namespace='CELERY'
)

celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
