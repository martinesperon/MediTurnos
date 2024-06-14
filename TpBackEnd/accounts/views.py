from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View

# Vista, basada en clases, para el usuario

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

class CustomLogoutView(View):
    """
    Custom logout view.
    """

    def get(self, request, *args, **kwargs):
        logout(request)
        # Redirigir a la página de login u otra página deseada
        return redirect('/')