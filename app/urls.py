from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodView, GroupViewSet, UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'foods', FoodView)
router.register(r'groups', GroupViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


# path('api/user-permissions/', views.UserGroupPermissionView.as_view(), name='user-permissions'),