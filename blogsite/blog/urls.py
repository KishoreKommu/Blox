from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('', views.dashboard, name='dashboard'),
    path('', views.post_list, name='post_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_create, name='post_create'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    path('about/', views.about, name='about'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')


]



