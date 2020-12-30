from django.urls import path
from . import views


urlpatterns = [path('', views.index, name='index'),
               path('jobs/', views.post_list, name='post_list'),
               path('post/<int:pk>/', views.post_detail, name='post_detail'),
               path('about-us/', views.about_us, name='about_us'),
               path('blogs/', views.blog_list, name='blog_list'),
               path('blogs/detail/<int:pk>', views.blog_detail, name='blog_detail'),
               path('terms/', views.terms, name='terms'),
               path('login/', views.login_user, name='login'),
               path('logout/', views.logout_user, name='logout'),
               path('register/', views.register_user, name='register'),
               path('contact-us/', views.contact_us, name='contact_us'),
               path('jobs/new/', views.post_new, name='post_new'),
               path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
               path('blogs/detail/new/', views.blog_new, name='blog_new'),
               path('blogs/detail/<int:pk>/edit', views.blog_edit, name='blog_edit'),
               path('jobs/categories/<str:cats>/', views.job_category, name='job_category'),
               path('jobs/search/', views.post_search, name='post_search'),
               path('blogs/search/', views.blog_search, name='blog_search'), ]
