from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FoodSerializer, GroupSerializer, UserSerializer
from .models import Food
from django.contrib.auth.models import Group, User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import CheckGroup

# Create your views here.

class FoodView(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    # permission_classes = [check_group('Restaurant_Admin')]
    permission_classes = [CheckGroup.for_group('Restaurant_Admin')]

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)