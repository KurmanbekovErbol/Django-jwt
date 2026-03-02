from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.testapp.views import TestModelViewSet

router = DefaultRouter()
router.register(r'test-models', TestModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]