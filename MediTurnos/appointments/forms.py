from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    """
    Formulario basado en clase, asociado al modelo Appointment.
    Validación de back-end (clean, heredado del model.clean()) +
    front-end (required, type=date/time).
    """

    class Meta:
        model = Appointment
        fields = ['date', 'time', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'required': True}),
            'time': forms.TimeInput(attrs={'type': 'time', 'required': True}),
            'reason': forms.TextInput(attrs={'required': True, 'minlength': 5, 'maxlength': 255}),
        }

    def clean_reason(self):
        reason = self.cleaned_data['reason'].strip()
        if len(reason) < 5:
            raise forms.ValidationError('Describí el motivo con al menos 5 caracteres.')
        return reason

    def clean(self):
        cleaned_data = super().clean()
        # Instancia temporal para reusar las validaciones de negocio del modelo
        instance = self.instance
        instance.date = cleaned_data.get('date')
        instance.time = cleaned_data.get('time')
        try:
            instance.clean()
        except Exception as e:
            raise forms.ValidationError(e)
        return cleaned_data


class AppointmentFilterForm(forms.Form):
    """
    Formulario SIN modelo asociado. Filtra el listado de turnos por
    estado y/o fecha vía query params (?status=&date_from=&date_to=).
    """
    status = forms.ChoiceField(
        choices=[('', 'Todos los estados')] + Appointment.STATUS_CHOICES,
        required=False,
        label='Estado'
    )
    date_from = forms.DateField(
        required=False, label='Desde', widget=forms.DateInput(attrs={'type': 'date'})
    )
    date_to = forms.DateField(
        required=False, label='Hasta', widget=forms.DateInput(attrs={'type': 'date'})
    )