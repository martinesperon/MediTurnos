from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import PatientProfile
from .forms import PatientProfileForm


class PatientProfileDetailView(LoginRequiredMixin, DetailView):
    """
    Muestra el perfil del paciente logueado. Autenticación validada en
    back-end (LoginRequiredMixin) y en front-end (el link solo se muestra
    a usuarios autenticados, ver base.html).
    """
    model = PatientProfile
    template_name = 'patients/patient_profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        profile, _created = PatientProfile.objects.get_or_create(user=self.request.user)
        return profile


class PatientProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    Alta/modificación del perfil del paciente (funciona como "alta" la
    primera vez, gracias a get_or_create, y como modificación después).
    """
    model = PatientProfile
    form_class = PatientProfileForm
    template_name = 'patients/patient_profile_form.html'
    success_url = reverse_lazy('patient_profile')

    def get_object(self, queryset=None):
        profile, _created = PatientProfile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        messages.success(self.request, 'Perfil actualizado correctamente.')
        return super().form_valid(form)