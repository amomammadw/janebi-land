from django.contrib import admin

from .models import ProductModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "is_active", "slug")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    list_editable = ("is_active",)
