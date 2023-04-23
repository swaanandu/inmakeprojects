from django.urls import path
from django.contrib import admin
from . import views
app_name='finance'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('move/', views.move, name='move'),
    path('new/',views.new,name='new'),
    path('success/', views.success, name='success'),

]