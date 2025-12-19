from django.db import models

class Appointment(models.Model):
    customer_name = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return f"{self.customer_name} - {self.service}"
