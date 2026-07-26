from django.urls import path
from . import views

urlpatterns = [
    path('', views.DoctorListView.as_view(), name='doctor_list'),
    path('nuevo/', views.DoctorCreateView.as_view(), name='doctor_create'),
    path('<int:pk>/', views.DoctorDetailView.as_view(), name='doctor_detail'),
    path('<int:pk>/editar/', views.DoctorUpdateView.as_view(), name='doctor_update'),
    path('<int:pk>/eliminar/', views.DoctorDeleteView.as_view(), name='doctor_delete'),
]