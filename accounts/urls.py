from django.urls import path
from .views import (
    register_user,
    get_users,
    get_user_detail,
    update_user,
    change_password,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', get_users, name='get_users'),
    path('users/<int:user_id>/', get_user_detail, name='get_user_detail'),
    path('users/<int:user_id>/update/', update_user, name='update_user'),
    path('users/change-password/', change_password, name='change_password'),
]