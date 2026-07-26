from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from doctors.models import Doctor


class Appointment(models.Model):
    """
    Relaciones uno a muchos: un Doctor tiene muchos turnos,
    un User (paciente) tiene muchos turnos.
    """

    STATUS_PENDING = 'pendiente'
    STATUS_CONFIRMED = 'confirmado'
    STATUS_CANCELLED = 'cancelado'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pendiente'),
        (STATUS_CONFIRMED, 'Confirmado'),
        (STATUS_CANCELLED, 'Cancelado'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField('Fecha')
    time = models.TimeField('Hora')
    reason = models.CharField('Motivo', max_length=255)
    status = models.CharField('Estado', max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField('Creado', auto_now_add=True)

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        ordering = ['date', 'time']

    def __str__(self):
        return f'{self.patient.username} - {self.doctor.name} - {self.date} {self.time}'

    def clean(self):
        if self.doctor_id and self.time:
            if not (self.doctor.available_from <= self.time <= self.doctor.available_to):
                raise ValidationError(
                    f'El médico solo atiende entre {self.doctor.available_from} y {self.doctor.available_to}.'
                )
        from datetime import date as date_cls
        if self.date and self.date < date_cls.today():
            raise ValidationError('La fecha del turno no puede ser en el pasado.')