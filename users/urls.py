from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='user-register'),
    path('user/', views.profile, name='profile'),

]