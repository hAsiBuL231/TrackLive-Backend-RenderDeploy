from rest_framework import serializers
from .models import UserModel, GroupModel

class UserSerializer(serializers.ModelSerializer):
    # user_id = serializers.ReadOnlyField()
    class Meta:
        model = UserModel
        fields = "__all__"

# class GroupSeralizer(serializers.HyperlinkedModelSerializer):
class GroupSeralizer(serializers.HyperlinkedModelSerializer):
    # groupId = serializers.ReadOnlyField()
    # users = UserSerializer(read_only=True, many = True)
    # users = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())
    class Meta:
        model = GroupModel
        # depth = 1
        fields = "__all__"
        # fields = ['url', 'groupId', 'name', 'imageUrl', 'users' ] 