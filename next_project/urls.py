from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('confirm/logout/', views.confirm_logout, name='confirm_logout'),
    path('register/', views.register, name='register'),
    path('detail/', views.detail, name='detail'),
]
