from django.urls import re_path, path
from homepage import views

urlpatterns = [
    re_path(r'^item/$', views.item, name='item'),
]
