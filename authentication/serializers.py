# serializers.py

from django.contrib.auth.models import User

from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = [
            "id", 
            "username", 
            # "first_name", 
            # "last_name", 
            "email", 
            "password", 
            # "is_active", 
            # "is_staff",
            # "date_joined"
        ]
        extra_kwargs = {"id": {"read_only": True}, "password": {"write_only": True}}
        # read_only_fields

    def create(self, validated_data):

        username = validated_data["username"]
        # first_name = validated_data["first_name"]
        # last_name = validated_data["last_name"]
        email = validated_data["email"]
        password = validated_data["password"]

        user = User.objects.create_user(
            username=username,
            # first_name=first_name,
            # last_name=last_name,
            email=email,
        )
        user.set_password(password)
        user.save()

        return user
    

from django.contrib.auth.models import User
from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
    """Login serializer"""        
    username = serializers.CharField(required=True)    
    password = serializers.CharField(required=True) # , read_only=True
    
class UserLoginResponseSerializer(serializers.ModelSerializer):
    """Response serializer"""        
    class Meta:        
        model = User  
        fields = ['id', 'email']
        # fields= "__all__"
        # fields = "id, username, first_name, last_name, email, password, is_active, is_staff"        
        # read_only_fields = ["id", "password", "is_active", "is_staff", "date_joined"]
        # exclude = ["password"]