from django.contrib import admin
from django.urls import path,include
from .views import home

app_name="homeview"
urlpatterns = [
    path('<str:username>',home,name='template'),
]
