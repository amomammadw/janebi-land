from django.urls import path, register_converter

from . import views
from .converters import UnicodeSlugConverter

register_converter(UnicodeSlugConverter, "uslug")

urlpatterns = [
    path("", views.product_list_view, name="product-list"),
    path("<uslug:slug>/", views.product_detail_view, name="product-detail"),
]
