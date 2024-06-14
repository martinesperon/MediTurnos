from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfileView
from django.contrib.auth import views as auth_views
from . import views


# Configuración de rutas para login y logout

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'), # vista de login
    path('logout/', views.CustomLogoutView.as_view(), name='logout'), # vista del logout
    path('profile/', ProfileView.as_view(), name='profile'),  # vista de perfil
]
