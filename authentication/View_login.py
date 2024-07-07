from django.contrib.auth.models import User
from authentication.serializers import UserLoginSerializer
from authentication.serializers import UserLoginResponseSerializer
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from django.contrib.auth import authenticate

class LoginView(APIView):
    """Login View"""
    permissions_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        login_serializer = UserLoginSerializer(data=request.data)

        if login_serializer.is_valid():
            user = authenticate(request, **login_serializer.data)
            if user is not None:
                response_class = UserLoginResponseSerializer(user)
                token, created_token = Token.objects.get_or_create(user_id=user.id)

                print("token: "+str(token))
            
                # if isinstance(created_token, Token):
                #     print("token2 : "+str(token))
                #     token = created_token
                return Response({
                        "status": {
                            "message": "User Authenticated",
                            "code": f"{status.HTTP_200_OK} OK" },
                        "token": token.key,
                        "user": response_class.data
                        })
            else:                
                raise serializers.ValidationError({
                    "error": {
                        "message": "Invalid Username or Password. Please try again",
                        "status": f"{status.HTTP_400_BAD_REQUEST} BAD REQUEST" }
                        })
        return Response({
            "error": login_serializer.errors,
            "status": f"{status.HTTP_403_FORBIDDEN} FORBIDDEN"
            })
