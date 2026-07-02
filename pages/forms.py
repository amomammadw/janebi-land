from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "phone", "email", "message"]
        labels = {
            "name": "نام",
            "phone": "موبایل",
            "email": "ایمیل (اختیاری)",
            "message": "پیام",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input", "placeholder": "نام شما"}),
            "phone": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "۰۹۱۲۳۴۵۶۷۸۹", "dir": "ltr"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-input", "placeholder": "email@example.com", "dir": "ltr"}
            ),
            "message": forms.Textarea(
                attrs={"class": "form-input", "placeholder": "پیام شما...", "rows": 5}
            ),
        }
