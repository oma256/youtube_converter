from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf import settings


urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include(('video_converter.urls', 'video_converter'),
                   namespace='video_converter'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

