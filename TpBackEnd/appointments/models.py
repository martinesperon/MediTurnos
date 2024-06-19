from django.db import models
from django.contrib.auth.models import User

class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    available_from = models.TimeField()
    available_to = models.TimeField()

    def __str__(self):
        return f"{self.name} ({self.specialty.name})"


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.patient.username} - {self.doctor.name} on {self.date} at {self.time}"