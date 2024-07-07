from django.urls import path

from . import views
from . import consumers

urlpatterns = [
    path("view", views.test, name="test"),
    path("ws", consumers.Consumer.as_asgi()),
]