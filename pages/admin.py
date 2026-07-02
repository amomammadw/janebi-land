from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "created_at")
    search_fields = ("name", "phone", "email", "message")
    readonly_fields = ("created_at",)
