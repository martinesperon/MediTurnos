from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Specialty
from .forms import SpecialtyForm, SpecialtySearchForm


class SpecialtyListView(ListView):
    """
    Listado público. Soporta filtro por query param ?q=texto (punto 5).
    """
    model = Specialty
    template_name = 'specialties/specialty_list.html'
    context_object_name = 'specialties'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.search_form = SpecialtySearchForm(self.request.GET or None)
        if self.search_form.is_valid():
            q = self.search_form.cleaned_data.get('q')
            if q:
                queryset = queryset.filter(name__icontains=q)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.search_form
        return context


class SpecialtyDetailView(DetailView):
    """Detalle público, accedido por parámetro de ruta <pk> (punto 5)."""
    model = Specialty
    template_name = 'specialties/specialty_detail.html'
    context_object_name = 'specialty'


class SpecialtyCreateView(LoginRequiredMixin, CreateView):
    model = Specialty
    form_class = SpecialtyForm
    template_name = 'specialties/specialty_form.html'
    success_url = reverse_lazy('specialty_list')

    def form_valid(self, form):
        messages.success(self.request, 'Especialidad creada correctamente.')
        return super().form_valid(form)


class SpecialtyUpdateView(LoginRequiredMixin, UpdateView):
    model = Specialty
    form_class = SpecialtyForm
    template_name = 'specialties/specialty_form.html'
    success_url = reverse_lazy('specialty_list')

    def form_valid(self, form):
        messages.success(self.request, 'Especialidad actualizada correctamente.')
        return super().form_valid(form)


class SpecialtyDeleteView(LoginRequiredMixin, DeleteView):
    model = Specialty
    template_name = 'specialties/specialty_confirm_delete.html'
    success_url = reverse_lazy('specialty_list')

    def form_valid(self, form):
        messages.success(self.request, 'Especialidad eliminada correctamente.')
        return super().form_valid(form)