from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_appointments, name='get_appointments'),      # GET
    path('add/', views.add_appointment, name='add_appointment'),    # POST
]
