from django import forms
from .models import Doctor


class DoctorForm(forms.ModelForm):
    """
    Formulario basado en clase, asociado al modelo Doctor.
    Validación de back-end en clean() (horario) + front-end (required, min/max).
    """

    class Meta:
        model = Doctor
        fields = ['name', 'license_number', 'specialties', 'available_from', 'available_to']
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
            'license_number': forms.TextInput(attrs={'required': True, 'pattern': r'^[A-Za-z0-9\-]{4,20}$'}),
            'specialties': forms.CheckboxSelectMultiple(),
            'available_from': forms.TimeInput(attrs={'type': 'time', 'required': True}),
            'available_to': forms.TimeInput(attrs={'type': 'time', 'required': True}),
        }

    def clean_specialties(self):
        specialties = self.cleaned_data.get('specialties')
        if not specialties or specialties.count() == 0:
            raise forms.ValidationError('Seleccioná al menos una especialidad.')
        return specialties

    def clean(self):
        cleaned_data = super().clean()
        available_from = cleaned_data.get('available_from')
        available_to = cleaned_data.get('available_to')
        if available_from and available_to and available_from >= available_to:
            raise forms.ValidationError(
                'El horario "desde" debe ser anterior al horario "hasta".'
            )
        return cleaned_data


class DoctorFilterForm(forms.Form):
    """
    Formulario SIN modelo asociado, para filtrar médicos por especialidad
    vía query param ?specialty=<id> (punto 5 y 9.4).
    """
    specialty = forms.ModelChoiceField(
        queryset=None,
        required=False,
        empty_label='Todas las especialidades',
        label='Especialidad'
    )

    def __init__(self, *args, **kwargs):
        from specialties.models import Specialty
        super().__init__(*args, **kwargs)
        self.fields['specialty'].queryset = Specialty.objects.all()