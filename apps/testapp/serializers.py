from rest_framework import serializers
from apps.testapp.models import TestModel

class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ['id', 'title', 'description', 'image', 'file']