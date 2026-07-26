from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Doctor
from .forms import DoctorForm, DoctorFilterForm


class DoctorListView(ListView):
    """Listado público, filtrable por query param ?specialty=<id>."""
    model = Doctor
    template_name = 'doctors/doctor_list.html'
    context_object_name = 'doctors'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('specialties')
        self.filter_form = DoctorFilterForm(self.request.GET or None)
        if self.filter_form.is_valid():
            specialty = self.filter_form.cleaned_data.get('specialty')
            if specialty:
                queryset = queryset.filter(specialties=specialty)
        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.filter_form
        return context


class DoctorDetailView(DetailView):
    """Detalle por parámetro de ruta <pk>."""
    model = Doctor
    template_name = 'doctors/doctor_detail.html'
    context_object_name = 'doctor'


class DoctorCreateView(LoginRequiredMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctor_form.html'
    success_url = reverse_lazy('doctor_list')

    def form_valid(self, form):
        messages.success(self.request, 'Médico creado correctamente.')
        return super().form_valid(form)


class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctor_form.html'
    success_url = reverse_lazy('doctor_list')

    def form_valid(self, form):
        messages.success(self.request, 'Médico actualizado correctamente.')
        return super().form_valid(form)


class DoctorDeleteView(LoginRequiredMixin, DeleteView):
    model = Doctor
    template_name = 'doctors/doctor_confirm_delete.html'
    success_url = reverse_lazy('doctor_list')

    def form_valid(self, form):
        messages.success(self.request, 'Médico eliminado correctamente.')
        return super().form_valid(form)