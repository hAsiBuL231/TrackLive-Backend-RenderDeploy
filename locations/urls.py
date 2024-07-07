from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('locations', views.LocationViewSet, basename= 'locations')

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URL patterns for the notes app
    path('locations/', include('rest_framework.urls', namespace='rest_framework')),
] 

# Create a file, notes/serializers.py with these lines:

# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from consumers import LocationConsumer

# application = ProtocolTypeRouter({
#     "websocket": AuthMiddlewareStack(
#         URLRouter([
#             path("ws/locations/", LocationConsumer.as_asgi()),
#         ])
#     ),
#     "http": router.urls,  # Use DRF router for HTTP requests
# })
# websocket_urlpatterns = [
#     path('ws/location/', LocationConsumer.as_asgi()),
# ]
