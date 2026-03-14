from modeltranslation.translator import register, TranslationOptions
from apps.testapp.models import TestModel

@register(TestModel)
class TestModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')