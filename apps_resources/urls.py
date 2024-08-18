from django.urls import path
from . import views

app_name = "resource"

urlpatterns = [
    path('upload_resource/', views.upload_resource, name='upload_resource'),
]