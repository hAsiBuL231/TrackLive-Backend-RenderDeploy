from django.urls import path

from . import consumers

ws_urlpatterns = [
    path("ws", consumers.Consumer.as_asgi())
]