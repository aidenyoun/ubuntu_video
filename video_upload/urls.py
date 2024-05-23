from django.urls import path
from . import views

urlpatterns = [
    path('uploadpc/', views.uploadpc, name='uploadpc'),
    path('upload_server/', views.upload_server, name='upload_server'),
]
