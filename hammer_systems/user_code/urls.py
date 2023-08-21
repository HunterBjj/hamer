from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('reg.html', views.reg, name='reg'),
]