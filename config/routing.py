from django.urls import path

from config.websocket import EchoConsumer
from config.websocket import NotificationConsumer
from config.websocket import websocket_application

websocket_routes = [
    path("", websocket_application),
    path("ws/echo/", EchoConsumer.as_asgi()),
    path("ws/notifications/", NotificationConsumer.as_asgi()),
]
