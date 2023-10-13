from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('auth2.html/', views.reg, name='reg'),
    path('main.html/', views.create, name='create'),
]