from django.contrib import admin
from .models import PatientProfile


@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'health_insurance', 'birth_date')
    search_fields = ('user__username', 'user__email', 'phone', 'health_insurance')
    list_filter = ('health_insurance',)
    ordering = ('user__username',)