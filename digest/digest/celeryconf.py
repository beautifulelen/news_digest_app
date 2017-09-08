from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digest.settings')

app = Celery('digest')

CELERY_TIMEZONE = 'UTC'
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'add-every-15-minutes': {
        'task': 'digest.tasks.get_rss',
        'schedule': 15*60,
    },
}
app.conf.timezone = 'UTC'
