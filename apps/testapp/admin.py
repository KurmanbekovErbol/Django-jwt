from django.contrib import admin
from apps.testapp.models import TestModel

@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    search_fields = ('title', 'description')

    