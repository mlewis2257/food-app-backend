from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FoodSerializer, GroupSerializer, UserSerializer
from .models import Food
from django.contrib.auth.models import Group, User
from .permissions import IsMemberOfGroup


from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class FoodView(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()



class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsMemberOfGroup]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer