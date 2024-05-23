from django.contrib import admin
from django.urls import path, include
import video_upload.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', video_upload.views.uploadpc, name='index'),
    path('video_upload/', include('video_upload.urls')),
]
