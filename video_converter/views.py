from django.shortcuts import render

from .forms import DownloadForm
from .tasks import convert_to_mp3


def index(request):
    if request.method == 'POST':
        host_name = request.META['HTTP_HOST']
        protocol = request.scheme
        form = DownloadForm(request.POST)
        if form.is_valid():
                url = form.cleaned_data.get('url')
                email = form.cleaned_data.get('email')
                convert_to_mp3.delay(url, email, host_name, protocol)
        return render(request, 'video_converter/index.html', {'form': form})
    form = DownloadForm()
    return render(request, 'video_converter/index.html', {'form': form})
