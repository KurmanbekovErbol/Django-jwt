from rest_framework import viewsets
from apps.testapp.models import TestModel
from apps.testapp.serializers import TestModelSerializer
from apps.users.permissions import IsAdmin, IsManager, IsTeacher, IsStudent 
from rest_framework.parsers import MultiPartParser

class TestModelViewSet(viewsets.ModelViewSet):
    """
    Простой ViewSet для просмотра и редактирования экземпляров TestModel.
    """
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer
    parser_classes = [MultiPartParser] 
    permission_classes = [IsAdmin | IsManager | IsTeacher | IsStudent]