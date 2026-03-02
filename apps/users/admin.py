from django.contrib import admin
from apps.users.models import CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = ('role', 'gender')
    search_fields = ('username', 'full_name', 'email')