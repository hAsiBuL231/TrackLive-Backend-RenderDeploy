from django.shortcuts import render

# Create your views here.
from .models import LocationModel
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import LocationSerializer
import json
from channels.layers import get_channel_layer
from channels.generic.websocket import async_to_sync

class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """
    queryset = LocationModel.objects.all().order_by('-created')
    serializer_class = LocationSerializer

    def create(self, request, *args, **kwargs):
        token = request.data.get('token')
        if not token:
            return Response({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['securityCode'] = token
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Send data to WebSocket Consumer
        # channel_layer = get_channel_layer()
        # async_to_sync(channel_layer.group_send)(
        #     "location_group",
        #     {
        #         "type": "location.message",
        #         "text": json.dumps(serializer.data)
        #     }
        # )
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)