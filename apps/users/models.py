from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Username must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE = (
        ("Administrator", "Администратор"),
        ("Manager", "Менеджер"),
        ("Teacher", "Преподаватель"),
        ("Student", "Ученик"),
    )
    GENDER = (
        ("Male", "Мужской"),
        ("Female", "Женский"),
        ("not indicated", "Не указан")
    )

    username = models.CharField(max_length=150, unique=True, verbose_name="Имя пользователя")
    full_name = models.CharField(max_length=255, blank=True, verbose_name="Полное имя")
    role = models.CharField(max_length=20, choices=ROLE, default="Student", verbose_name="Роль")
    age = models.CharField(max_length=3, verbose_name="Возраст")
    avatarka = models.FileField(upload_to="avatarka/", verbose_name="Изображение Профиля", blank=False, null=True)
    email = models.EmailField(unique=True, verbose_name="Email", blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER, default="not indicated", verbose_name="Пол")

    is_active = models.BooleanField(default=True, verbose_name="Активный")
    is_staff = models.BooleanField(default=False, verbose_name="Статус персонала")

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
            return f"{self.username} ({self.role})"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"