from django.db import models

from base.models import BaseTimestampModel, BaseUUIDModel


class ProductModel(BaseUUIDModel, BaseTimestampModel):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, allow_unicode=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    discount = models.IntegerField(null=True, blank=True, default=None)
    has_loan = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
