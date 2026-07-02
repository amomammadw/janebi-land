from django.contrib import messages
from django.shortcuts import redirect, render

from products.models import ProductModel

from .forms import ContactForm


def home_view(request):
    featured_products = ProductModel.objects.filter(is_active=True)[:8]
    return render(request, "pages/home.html", {"featured_products": featured_products})


def about_view(request):
    return render(request, "pages/about.html")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "پیام شما با موفقیت ارسال شد.")
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "pages/contact.html", {"form": form})
