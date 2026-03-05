from rest_framework import generics, permissions
from drf_yasg.utils import swagger_auto_schema
from apps.users.models import CustomUser
from apps.users.serializers import RegisterSerializer, TokenResponseSerializer, UserProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.parsers import FormParser, MultiPartParser

# Создаем кастомный рефреш для красивого Swagger
class CustomTokenRefreshView(TokenRefreshView):
    parser_classes = [FormParser, MultiPartParser]

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    parser_classes = [MultiPartParser] 

class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser]

    def get_object(self):
        return self.request.user

    @swagger_auto_schema(consumes=['multipart/form-data'])
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(consumes=['multipart/form-data'])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    parser_classes = [FormParser, MultiPartParser]

    @swagger_auto_schema(
        responses={200: TokenResponseSerializer},
        operation_description="Вход в систему. Возвращает пару JWT токенов."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class CustomTokenRefreshView(TokenRefreshView):
    parser_classes = [FormParser, MultiPartParser]
    
    @swagger_auto_schema(
        # Для рефреша обычно возвращается только новый access токен, 
        # но структура похожа (зависит от настроек SimpleJWT)
        responses={200: TokenResponseSerializer}, 
        operation_description="Обновление access токена через refresh токен."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)