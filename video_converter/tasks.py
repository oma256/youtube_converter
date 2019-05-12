from __future__ import absolute_import, unicode_literals

from django.core.mail import send_mail
from django.conf import settings
from config.celery import app

import youtube_dl


download_url = ''


@app.task
def convert_to_mp3(url, email):
    path_to_file = f'{settings.MEDIA_ROOT}/mp3/%(title)s.mp3'
    print(path_to_file)
    options = {
        'extractaudio': True,
        'audioformat': "mp3",
        'outtmpl': 'media/%(id)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        r = ydl.extract_info(url, download=True)

    file_dir = 'http://0.0.0.0:8000/media/{}'.format(r['id'])
    send_email.delay(email, file_dir)


@app.task
def send_email(email, file_dir):
    subject = 'Converter to mp3'
    message = file_dir + '.mp3'
    email_from = settings.EMAIL_HOST_USER
    email_to = [email]
    send_mail(subject, message, email_from, email_to)

