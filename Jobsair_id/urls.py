from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [path('', views.post_list, name='post_list'), ]

urlpatterns += staticfiles_urlpatterns()
