from django.shortcuts import get_object_or_404, render

from .models import ProductModel


def product_list_view(request):
    products = ProductModel.objects.filter(is_active=True)
    return render(request, "products/list.html", {"products": products})


def product_detail_view(request, slug):
    product = get_object_or_404(ProductModel, slug=slug, is_active=True)
    return render(request, "products/detail.html", {"product": product})
