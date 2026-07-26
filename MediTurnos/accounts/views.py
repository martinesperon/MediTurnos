from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from .forms import RegisterForm


class ProfileView(LoginRequiredMixin, TemplateView):
    """Vista basada en clase. Autenticación validada en back-end (mixin)
    y en front-end (link solo visible logueado, ver base.html)."""
    template_name = 'accounts/profile.html'


class RegisterView(CreateView):
    """Alta de usuario (formulario basado en clase, ligado al modelo User)."""
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, f'¡Bienvenido, {self.object.username}!')
        return response


class CustomLogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')