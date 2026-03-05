from django.urls import path
from apps.users.views import RegisterView, ProfileView, CustomTokenObtainPairView, CustomTokenRefreshView


urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('profile/', ProfileView.as_view(), name='user_profile'),
]