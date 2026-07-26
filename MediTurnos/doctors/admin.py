from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_number', 'specialties_display', 'available_from', 'available_to')
    search_fields = ('name', 'license_number', 'specialties__name')
    list_filter = ('specialties', 'available_from')
    ordering = ('name',)
    filter_horizontal = ('specialties',)