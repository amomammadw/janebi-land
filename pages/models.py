from django.db import models

from accounts.models import validate_iranian_phone


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    phone = models.CharField(max_length=11, validators=[validate_iranian_phone], verbose_name="موبایل")
    email = models.EmailField(blank=True, verbose_name="ایمیل")
    message = models.TextField(verbose_name="پیام")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "پیام تماس"
        verbose_name_plural = "پیام‌های تماس"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.phone}"
