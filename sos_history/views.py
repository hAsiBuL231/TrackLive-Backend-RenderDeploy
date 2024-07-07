from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import SOSHistory
from .serializers import SOSHistorySerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

class SOSHistoryViewSet(viewsets.ModelViewSet):
    queryset = SOSHistory.objects.all().order_by('-created')
    serializer_class = SOSHistorySerializer


    def create(self, request, *args, **kwargs):
        token = request.data.get('token')
        if not token:
            return Response({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['securityCode'] = token
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)