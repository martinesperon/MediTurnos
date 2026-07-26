from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
from doctors.models import Doctor
from .models import Appointment
from .forms import AppointmentForm, AppointmentFilterForm


class AppointmentListView(LoginRequiredMixin, ListView):
    """
    Lista únicamente los turnos del usuario logueado. Autenticación
    validada en back-end (LoginRequiredMixin) y front-end (link oculto
    en base.html si no hay sesión). Filtrable por query params.
    """
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointments'
    paginate_by = 10

    def get_queryset(self):
        queryset = Appointment.objects.filter(patient=self.request.user).select_related('doctor')
        self.filter_form = AppointmentFilterForm(self.request.GET or None)
        if self.filter_form.is_valid():
            status = self.filter_form.cleaned_data.get('status')
            date_from = self.filter_form.cleaned_data.get('date_from')
            date_to = self.filter_form.cleaned_data.get('date_to')
            if status:
                queryset = queryset.filter(status=status)
            if date_from:
                queryset = queryset.filter(date__gte=date_from)
            if date_to:
                queryset = queryset.filter(date__lte=date_to)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.filter_form
        return context


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    """Detalle por parámetro de ruta <pk>, restringido al dueño del turno."""
    model = Appointment
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user)


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    """Crea un turno para el médico indicado por parámetro de ruta <doctor_id>."""
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

    def dispatch(self, request, *args, **kwargs):
        self.doctor = get_object_or_404(Doctor, pk=kwargs['doctor_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.doctor = self.doctor
        form.instance.patient = self.request.user
        messages.success(self.request, 'Turno reservado correctamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctor'] = self.doctor
        return context


class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Turno actualizado correctamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctor'] = self.object.doctor
        return context


class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Appointment
    template_name = 'appointments/appointment_confirm_delete.html'
    success_url = reverse_lazy('appointment_list')

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Turno cancelado correctamente.')
        return super().form_valid(form)