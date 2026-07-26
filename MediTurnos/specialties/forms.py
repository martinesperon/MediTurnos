from django import forms
from .models import Specialty


class SpecialtyForm(forms.ModelForm):
    """
    Formulario basado en clase, asociado al modelo Specialty.
    Validación de back-end en clean_name + atributos HTML de front-end.
    """

    class Meta:
        model = Specialty
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'required': True,
                'minlength': 3,
                'placeholder': 'Ej: Cardiología',
            }),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if len(name) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return name.capitalize()


class SpecialtySearchForm(forms.Form):
    """
    Formulario SIN modelo asociado (punto 9.4). Se usa para el buscador
    del listado, vía query param ?q=
    """
    q = forms.CharField(
        label='Buscar',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Buscar por nombre...'})
    )