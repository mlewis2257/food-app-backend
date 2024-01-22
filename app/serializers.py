from rest_framework import serializers
from .models import Food
from django.contrib.auth.models import User, Group


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('title', 'description', 'completed')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

# class UserSerializer(serializers.ModelSerializer):
#     groups = GroupSerializer(many=True, read_only=True)

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'groups']
        
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name', 'groups']

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'groups']

    def get_groups(self, obj):
        return [group.name for group in obj.groups.all()]