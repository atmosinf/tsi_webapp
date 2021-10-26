from django.urls import re_path, path
from homepage import views

app_name='homepage'

urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^logout/$', views.user_logout, name='logout'),
    re_path(r'^login/$', views.user_login, name='user_login'),
    re_path(r'^(?P<pk>\d+)/$',views.ItemDetailView.as_view(),name='detail'),
]
