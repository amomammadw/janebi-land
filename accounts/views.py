import json
import random
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth import login
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import validate_iranian_phone, User

OTP_SESSION_KEY = "otp_data"
OTP_EXPIRY_MINUTES = 5


def _json_error(message, status=400):
    return JsonResponse({"success": False, "error": message}, status=status)


@require_POST
def send_otp_view(request):
    try:
        data = json.loads(request.body)
        phone = data.get("phone", "").strip()
    except (json.JSONDecodeError, AttributeError):
        return _json_error("درخواست نامعتبر است.")

    try:
        validate_iranian_phone(phone)
    except Exception:
        return _json_error("شماره موبایل معتبر نیست.")

    dev_code = getattr(settings, "OTP_DEV_CODE", None)
    code = dev_code or f"{random.randint(100000, 999999)}"

    request.session[OTP_SESSION_KEY] = {
        "phone": phone,
        "code": code,
        "expires": (timezone.now() + timedelta(minutes=OTP_EXPIRY_MINUTES)).isoformat(),
    }
    request.session.modified = True

    print(f"[OTP] phone={phone} code={code}")

    return JsonResponse({"success": True, "message": "کد تأیید ارسال شد."})


@require_POST
def verify_otp_view(request):
    try:
        data = json.loads(request.body)
        phone = data.get("phone", "").strip()
        code = data.get("code", "").strip()
    except (json.JSONDecodeError, AttributeError):
        return _json_error("درخواست نامعتبر است.")

    otp_data = request.session.get(OTP_SESSION_KEY)
    if not otp_data:
        return _json_error("کد تأیید منقضی شده است. دوباره تلاش کنید.")

    expires = datetime.fromisoformat(otp_data["expires"])
    if timezone.is_naive(expires):
        expires = timezone.make_aware(expires)

    if timezone.now() > expires:
        del request.session[OTP_SESSION_KEY]
        return _json_error("کد تأیید منقضی شده است. دوباره تلاش کنید.")

    if otp_data["phone"] != phone or otp_data["code"] != code:
        return _json_error("کد تأیید اشتباه است.")

    user, _ = User.objects.get_or_create(phone=phone)
    login(request, user)

    del request.session[OTP_SESSION_KEY]

    return JsonResponse({"success": True, "message": "ورود با موفقیت انجام شد."})
