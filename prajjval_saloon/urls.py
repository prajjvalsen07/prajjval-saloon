from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

# Salon website views
from prajjval_saloon import views as core_views
from . import views  # for salon_products

urlpatterns = [
    # =======================
    # 🌐 SALON WEBSITE PAGES
    # =======================
    path("", core_views.index, name="home"),
    path("about/", core_views.about, name="about"),
    path("service/", core_views.service, name="service"),
    path("team/", core_views.team, name="team"),
    path("testimonial/", core_views.testimonial, name="testimonial"),
    path("contact/", core_views.contact, name="contact"),
    path("error/", core_views.error, name="error"),
    path("blog/", core_views.blog, name="blog"),

    # Salon products (Makeup API page)
    path("salon-products/", views.salon_products, name="salon_products"),

    # =======================
    # 🔌 APPOINTMENT API (DRF)
    # =======================
    path("api/appointments/", include("appointments.urls")),

    # =======================
    # 🔐 ADMIN
    # =======================
    path("admin/", admin.site.urls),

    # =======================
    # 🔁 REDIRECTS (OLD LINKS)
    # =======================
    path("about/index.html", RedirectView.as_view(pattern_name="about", permanent=True)),
    path("service/index.html", RedirectView.as_view(pattern_name="service", permanent=True)),
    path("team/index.html", RedirectView.as_view(pattern_name="team", permanent=True)),
    path("testimonial/index.html", RedirectView.as_view(pattern_name="testimonial", permanent=True)),
    path("contact/index.html", RedirectView.as_view(pattern_name="contact", permanent=True)),
]

# =======================
# 📂 STATIC & MEDIA (DEV)
# =======================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
