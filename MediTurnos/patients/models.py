from django.db import models
from django.contrib.auth.models import User


class PatientProfile(models.Model):
    """
    Perfil extendido del paciente. Relación uno a uno con el modelo User de Django.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )
    phone = models.CharField('Teléfono', max_length=20, blank=True)
    birth_date = models.DateField('Fecha de nacimiento', null=True, blank=True)
    health_insurance = models.CharField('Obra social', max_length=100, blank=True)
    address = models.CharField('Dirección', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Perfil de paciente'
        verbose_name_plural = 'Perfiles de pacientes'
        ordering = ['user__username']

    def __str__(self):
        return f'Perfil de {self.user.username}'