function getCsrfToken() {
  const cookie = document.cookie
    .split(";")
    .map((c) => c.trim())
    .find((c) => c.startsWith("csrftoken="));
  return cookie ? decodeURIComponent(cookie.split("=")[1]) : "";
}

function openSignupModal() {
  document.getElementById("signup-modal").classList.add("active");
  showStep("phone");
  clearErrors();
}

function closeSignupModal() {
  document.getElementById("signup-modal").classList.remove("active");
}

function showStep(step) {
  document.getElementById("otp-step-phone").classList.toggle("hidden", step !== "phone");
  document.getElementById("otp-step-code").classList.toggle("hidden", step !== "code");
}

function clearErrors() {
  document.getElementById("otp-error").textContent = "";
  document.getElementById("otp-error").classList.add("hidden");
}

function showError(message) {
  const el = document.getElementById("otp-error");
  el.textContent = message;
  el.classList.remove("hidden");
}

async function sendOtp() {
  clearErrors();
  const phone = document.getElementById("otp-phone").value.trim();
  const btn = document.getElementById("otp-send-btn");
  btn.disabled = true;

  try {
    const res = await fetch("/accounts/otp/send/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCsrfToken(),
      },
      body: JSON.stringify({ phone }),
    });
    const data = await res.json();
    if (data.success) {
      document.getElementById("otp-phone-display").textContent = phone;
      showStep("code");
    } else {
      showError(data.error || "خطایی رخ داد.");
    }
  } catch {
    showError("خطا در ارتباط با سرور.");
  } finally {
    btn.disabled = false;
  }
}

async function verifyOtp() {
  clearErrors();
  const phone = document.getElementById("otp-phone").value.trim();
  const code = document.getElementById("otp-code").value.trim();
  const btn = document.getElementById("otp-verify-btn");
  btn.disabled = true;

  try {
    const res = await fetch("/accounts/otp/verify/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCsrfToken(),
      },
      body: JSON.stringify({ phone, code }),
    });
    const data = await res.json();
    if (data.success) {
      window.location.reload();
    } else {
      showError(data.error || "خطایی رخ داد.");
    }
  } catch {
    showError("خطا در ارتباط با سرور.");
  } finally {
    btn.disabled = false;
  }
}

function toggleMobileNav() {
  document.getElementById("mobile-nav").classList.toggle("open");
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("signup-open-btn")?.addEventListener("click", openSignupModal);
  document.getElementById("signup-close-btn")?.addEventListener("click", closeSignupModal);
  document.getElementById("signup-modal")?.addEventListener("click", (e) => {
    if (e.target.id === "signup-modal") closeSignupModal();
  });
  document.getElementById("otp-send-btn")?.addEventListener("click", sendOtp);
  document.getElementById("otp-verify-btn")?.addEventListener("click", verifyOtp);
  document.getElementById("otp-back-btn")?.addEventListener("click", () => showStep("phone"));
  document.getElementById("mobile-menu-btn")?.addEventListener("click", toggleMobileNav);
});
