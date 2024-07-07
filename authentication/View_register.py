from django.shortcuts import render

# Create your views here.

# views.py

from django.contrib.auth.models import User
from yaml import serializer, serialize, serialize_all

from authentication.serializers import RegistrationSerializer

from rest_framework import serializers
from rest_framework.views import APIView, View
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework import permissions


class RegistrationView(APIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    """Registeration View"""

    def get(self, request, pk=None, format=None):
        if pk is not None:
            queryset = User.objects.get(id = pk)       #complex data
            serializer = RegistrationSerializer(queryset)      #python dictionary convertion
            return Response(serializer.data)
        # else
        queryset = User.objects.all()
        print(queryset)
        serializer = RegistrationSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Handles post request logic"""
        registration_serializer  = RegistrationSerializer(data=request.data)

        # Generate tokens for existing users
        for user in User.objects.all():
            if not user:
                break
            else:
                try:
                    Token.objects.get(user_id=user.id)
                except Token.DoesNotExist:
                    Token.objects.create(user=user)

        if registration_serializer.is_valid(raise_exception=True):
            user = registration_serializer.save()
            token = Token.objects.create(user=user)

            return Response(
                {
                    "status": {
                        "message": "User created",
                        "code": f"{status.HTTP_200_OK} OK",
                    },
                    "token": token.key,
                    "user": {
                        "id": registration_serializer.data["id"],
                        # "first_name": registration_serializer.data["first_name"],
                        # "last_name": registration_serializer.data["last_name"],
                        "username": registration_serializer.data["username"],
                        "email": registration_serializer.data["email"],
                        # "is_active": registration_serializer.data["is_active"],
                        # "is_staff": registration_serializer.data["is_staff"],
                    },
                }
            )
        return Response(
             {
                "error": serializer.errors,
                # "status": f"{status.HTTP_203_NON_AUTHORITATIVE_INFORMATION} \ 
                #     NON AUTHORITATIVE INFORMATION",
                "status": { "msg": "NON AUTHORITATIVE INFORMATION", "code": status.HTTP_203_NON_AUTHORITATIVE_INFORMATION}
            }
        )
    
    def put(self, request, pk, format=None):
        if pk is not None:
            user = User.objects.get(id = pk)                           #complex data
            registration_serializer = RegistrationSerializer(user, data=request.data)       #python dictionary convertion
            

            if registration_serializer.is_valid(raise_exception=True):
                user = registration_serializer.save()
                token = Token.objects.get(user_id=user.id)

                return Response(
                    {
                        "user": {
                            "id": registration_serializer.data["id"],
                            # "first_name": registration_serializer.data["first_name"],
                            # "last_name": registration_serializer.data["last_name"],
                            "username": registration_serializer.data["username"],
                            "email": registration_serializer.data["email"],
                        },
                        "status": {
                            "message": "User updated",
                            "code": f"{status.HTTP_200_OK} OK",
                        },
                        "token": token.key,
                    }
                )
            return Response(
                {
                    "error": registration_serializer.errors,
                    "status": { "msg": "NON AUTHORITATIVE INFORMATION", "code": status.HTTP_203_NON_AUTHORITATIVE_INFORMATION}
                }
            )        

