from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("phone", "is_active", "is_staff", "created_at")
    list_filter = ("is_active", "is_staff")
    search_fields = ("phone",)
    ordering = ("-created_at",)

    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        ("دسترسی‌ها", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("phone", "password1", "password2", "is_staff", "is_superuser")}),
    )
