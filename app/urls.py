from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('notification', views.send_notification, name="notification"),

]