from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class TestModel(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    description = CKEditor5Field(verbose_name="Описание", config_name='extends')
    image = models.ImageField(verbose_name="Изображение", upload_to='test_images/', blank=True, null=True)
    file = models.FileField(verbose_name="Файл", upload_to='test_files/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Тестовая модель"
        verbose_name_plural = "Тестовые модели"