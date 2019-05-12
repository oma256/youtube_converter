from __future__ import absolute_import
import os

from django.conf import settings

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


app = Celery('youtube', broker='redis://redis:6379')
app.config_from_object('django.conf.settings')

app.autodiscover_tasks(settings.INSTALLED_APPS)


def debug_task(self):
    print('Request: {0!r}'.format(self.request))
