from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import UserModel, GroupModel
from .serializers import UserSerializer, GroupSeralizer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSeralizer

    # # companies/{id}/employees/
    # @action(detail=True, methods=['get'])
    # def employees(self, request, pk=None):
    #     try:
    #         group = GroupModel.objects.get(pk=pk)
    #         users = UserModel.objects.filter(users = group)
    #         user_serializer = UserSeralizer(users, many = True, context={'request': request})
    #         return Response(user_serializer.data)
    #     except Exception as e:
    #         return Response({'error': 'Company might not exits!!'})


    # def retrieve(self, request, *args, **kwargs):
    #     users = Token.objects.get(key=request).user
    #     user = UserModel.objects.get(email=users['email'])

    #     serializer = self.get_serializer(user)
    #     return Response(serializer.data)

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import UserModel
from rest_framework.authtoken.models import Token

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

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
    
    # user/{id}/groups/
    @action(detail=True, methods=['get'])
    def groups(self, request, pk=None):
        try:
            user = UserModel.objects.get(pk=pk)
            groups = GroupModel.objects.filter(users = user)
            group_serializer = GroupSeralizer(groups, many = True, context={'request': request})
            return Response(group_serializer.data)
        except Exception as e:
            return Response({'error': 'Group might not exits!!'})



    # {
    #   "username": "Hasibul",
    #   "password": "123456"
    # }





