from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gopickey, name='gopickey'),
    path('pickyweb', views.gopickey, name='gopickey'),
    path('home', views.home, name='home'),
    # path('add/', views.add, name='add'),
    path('add/<int:pk>', views.addone, name='addone'),
    path('<int:pk>', views.addone, name='addone'),
    path('Password', views.Password, name='Password'),
]
