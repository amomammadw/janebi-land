from django.urls import path

from . import views

urlpatterns = [
    path("otp/send/", views.send_otp_view, name="otp-send"),
    path("otp/verify/", views.verify_otp_view, name="otp-verify"),
]
