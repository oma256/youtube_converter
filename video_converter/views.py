from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect

import youtube_dl
from django.conf import settings

from .forms import DownloadForm
from .tasks import convert_to_mp3, send_email


def index(request):
    if request.method == 'POST':
        form = DownloadForm(request.POST)
        if form.is_valid():
                url = form.cleaned_data.get('url')
                email = form.cleaned_data.get('email')
                convert_to_mp3.delay(url, email)
        return render(request, 'video_converter/index.html', {'form': form})
    form = DownloadForm()
    return render(request, 'video_converter/index.html', {'form': form})
