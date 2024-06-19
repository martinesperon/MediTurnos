from django.urls import path
from . import views

urlpatterns = [
    path('oftalmologia/', views.specialty_doctors, {'specialty_name': 'Oftalmología'}, name='specialty_doctors'),
    path('book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('success/', views.appointment_success, name='appointment_success'),
    path('specialty/<str:specialty_name>/', views.specialty_doctors, name='specialty_doctors'),
]
