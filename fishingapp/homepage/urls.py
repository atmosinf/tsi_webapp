from django.urls import re_path, path
from homepage import views

app_name='homepage'

urlpatterns = [
    re_path(r'^item/$', views.item, name='item'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^logout/$', views.user_logout, name='logout'),
    re_path(r'^login/$', views.user_login, name='user_login'),
]
