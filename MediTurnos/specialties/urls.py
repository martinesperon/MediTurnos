from django.urls import path
from . import views

urlpatterns = [
    path('', views.SpecialtyListView.as_view(), name='specialty_list'),
    path('nueva/', views.SpecialtyCreateView.as_view(), name='specialty_create'),
    path('<int:pk>/', views.SpecialtyDetailView.as_view(), name='specialty_detail'),
    path('<int:pk>/editar/', views.SpecialtyUpdateView.as_view(), name='specialty_update'),
    path('<int:pk>/eliminar/', views.SpecialtyDeleteView.as_view(), name='specialty_delete'),
]