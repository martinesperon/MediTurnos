from django.db import models
from specialties.models import Specialty

class Doctor(models.Model):
    """
    Un médico puede atender varias especialidades, y una especialidad
    puede tener varios médicos -> relación muchos a muchos (punto 10).
    """
    name = models.CharField('Nombre completo', max_length=100)
    license_number = models.CharField('N° de matrícula', max_length=20, unique=True)
    specialties = models.ManyToManyField(
        Specialty,
        related_name='doctors',
        verbose_name='Especialidades'
    )
    available_from = models.TimeField('Disponible desde')
    available_to = models.TimeField('Disponible hasta')

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
        ordering = ['name']

    def __str__(self):
        return self.name

    def specialties_display(self):
        return ', '.join(s.name for s in self.specialties.all())
    specialties_display.short_description = 'Especialidades'