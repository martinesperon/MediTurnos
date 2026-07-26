from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    path('accounts/', include('accounts.urls')),
    path('patients/', include('patients.urls')),
    path('specialties/', include('specialties.urls')),
    path('doctors/', include('doctors.urls')),
    path('appointments/', include('appointments.urls')),
]
