from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppointmentListView.as_view(), name='appointment_list'),
    path('nuevo/<int:doctor_id>/', views.AppointmentCreateView.as_view(), name='appointment_create'),
    path('<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment_detail'),
    path('<int:pk>/editar/', views.AppointmentUpdateView.as_view(), name='appointment_update'),
    path('<int:pk>/eliminar/', views.AppointmentDeleteView.as_view(), name='appointment_delete'),
]