from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from ourservice.models import AboutUs, Service, review, Contactform


# ================= HOME =================
def homepage(request):
    data = {
        'about_d': AboutUs.objects.all(),
        'service_d': Service.objects.all(),
        'reviewdata': review.objects.all(),
    }
    return render(request, 'index.html', data)


def index(request):
    return render(request, "index.html")


# ================= STATIC PAGES =================
def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def team(request):
    return render(request, 'team.html')


def error(request):
    return render(request, '404.html')


def blog(request):
    return render(request, "blog.html")



# ================= CONTACT (FINAL) =================
def contact(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()

        if not (fullname and email and message):
            messages.error(request, "Please fill all required fields.")
            return redirect('contact')

        Contactform.objects.create(
            fullname=fullname,
            email=email,
            phone=phone,
            message=message,
        )

        try:
            send_mail(
                subject=f"[SALONE CONTACT] {fullname}",
                message=f"""
New Contact Message

Name: {fullname}
Email: {email}
Phone: {phone}

Message:
{message}
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["prajjvalsen3@gmail.com"],
                fail_silently=False,
            )
        except Exception as e:
            messages.error(request, f"Saved but mail failed: {e}")
            return redirect('contact')

        send_mail(
            subject="Thanks for contacting Salone",
            message="We received your message and will get back to you shortly.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=True,
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, "contact.html")
import requests
from django.shortcuts import render


def salon_products(request):
    api_url = "https://makeup-api.herokuapp.com/api/v1/products.json"

    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            products = response.json()[:20]  # sirf 20 products (fast & clean)
        else:
            products = []
    except Exception:
        products = []

    return render(request, "salon_products.html", {"products": products})
