from django.urls import path
from . import views


urlpatterns = [path('', views.index, name='index'),
               path('jobs/', views.post_list, name='post_list'),
               path('login/', views.login_user, name='login'),
               path('register/', views.register_user, name='register'),
               path('post/<int:pk>/', views.post_detail, name='post_detail'), ]
