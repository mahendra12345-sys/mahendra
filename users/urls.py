from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserListCreateView
from .auth_views import CustomTokenObtainPairView, logout_view

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', logout_view, name='logout'),
]
