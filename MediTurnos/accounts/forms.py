from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """
    Formulario basado en clase, asociado al modelo User.
    UserCreationForm ya trae validación de back-end (contraseñas
    coincidentes, fortaleza, username único); acá sumamos email
    obligatorio y su validación de front-end.
    """
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'required': True}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Ya existe una cuenta con ese email.')
        return email