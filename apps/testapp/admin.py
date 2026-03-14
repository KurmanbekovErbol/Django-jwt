from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import TestModel

@admin.register(TestModel)
class TestModelAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'image', 'file')
    search_fields = ('title',)