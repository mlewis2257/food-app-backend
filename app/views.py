from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FoodSerializer, GroupSerializer, UserSerializer, UserRegistrationSerializer
from .models import Food
from django.contrib.auth.models import Group, User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import CheckGroup
from rest_framework_simplejwt.tokens import RefreshToken
# import logging

# logger = logging.getLogger(__name__)

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

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        # logger.info(f"Received Signup Request: {request.data}")
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                # 'user': {
                #     'username': user.username,
                #     'email': user.email,
                #     'groups': user.groups,
                # },
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)