from django import forms
from .models import PatientProfile


class PatientProfileForm(forms.ModelForm):
    """
    Formulario basado en clase, asociado al modelo PatientProfile.
    Incluye validación de back-end (clean_phone) además de los atributos
    HTML de validación de front-end (required, pattern).
    """

    class Meta:
        model = PatientProfile
        fields = ['phone', 'birth_date', 'health_insurance', 'address']
        widgets = {
            'phone': forms.TextInput(attrs={
                'required': True,
                'pattern': r'^[0-9\-\+\s]{6,20}$',
                'title': 'Solo números, espacios, + y -',
            }),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'required': True}),
            'health_insurance': forms.TextInput(attrs={'required': True}),
            'address': forms.TextInput(attrs={'required': True}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        digits = ''.join(ch for ch in phone if ch.isdigit())
        if len(digits) < 6:
            raise forms.ValidationError('El teléfono debe tener al menos 6 dígitos.')
        return phone

    def clean_birth_date(self):
        from datetime import date
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date and birth_date > date.today():
            raise forms.ValidationError('La fecha de nacimiento no puede ser futura.')
        return birth_date