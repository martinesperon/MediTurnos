from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientProfileDetailView.as_view(), name='patient_profile'),
    path('editar/', views.PatientProfileUpdateView.as_view(), name='patient_profile_edit'),
]