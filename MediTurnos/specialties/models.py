from django.db import models

class Specialty(models.Model):
    name = models.CharField('Nombre', max_length=100, unique=True)
    description = models.TextField('Descripción', blank=True)
    created_at = models.DateTimeField('Fecha de creación', auto_now_add=True)

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'
        ordering = ['name']

    def __str__(self):
        return self.name