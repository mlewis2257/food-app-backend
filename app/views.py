from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FoodSerializer, GroupSerializer, UserSerializer
from .models import Food
from django.contrib.auth.models import Group, User


from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class FoodView(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()



class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer