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

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'groups']