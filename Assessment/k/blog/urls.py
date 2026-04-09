from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('like/<int:pk>/', views.like_post, name='like_post'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('comment/<int:pk>/', views.add_comment, name='add_comment'),
    path('delete-comment/<int:id>/', views.delete_comment, name='delete_comment'),
]