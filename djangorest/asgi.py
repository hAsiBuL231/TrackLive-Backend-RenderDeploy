"""
ASGI config for djangorest project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangorest.settings')

# application = get_asgi_application()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from Test import routing
from django.urls import path
from Test.consumers import Consumer

application = ProtocolTypeRouter({
    # "http": get_asgi_application(),
    "http": URLRouter([
        path("sse", Consumer.as_asgi()),
        path(r"", get_asgi_application),
    ]),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.ws_urlpatterns
        )
    ),
})