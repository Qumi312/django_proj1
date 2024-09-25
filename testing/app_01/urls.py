from django.urls import path

from app_01 import views


app_name = 'logg'


urlpatterns = [
    path('', views.upload_file),
    path('list/', views.list_logs)
]