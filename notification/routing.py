from django.urls import path

from app.consumer import NotificationConsumer

websocket_urlpatterns = [
    path("ws/notification/<str:id>/", NotificationConsumer.as_asgi())
]