# labs/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='labs/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='labs/logout.html'), name='logout'),
    path('logout/', views.custom_logout, name='logout'),
    
    path('laboratorios/', views.LaboratorioListView.as_view(), name='laboratorios'),
    path('laboratorio/<int:pk>/', views.laboratorio_detail, name='laboratorio_detail'),
    
    path('reservar/', views.reservar_laboratorio, name='reservar'),
    path('minhas-reservas/', views.minhas_reservas, name='minhas_reservas'),
    path('cancelar-reserva/<int:pk>/', views.cancelar_reserva, name='cancelar_reserva'),

    # Admin URLs
    path('admin/laboratorios/', views.admin_laboratorios, name='admin_laboratorios'),
    path('admin/laboratorios/add/', views.admin_add_laboratorio, name='admin_add_laboratorio'),
    path('admin/laboratorios/edit/<int:pk>/', views.admin_edit_laboratorio, name='admin_edit_laboratorio'),
    path('admin/laboratorios/delete/<int:pk>/', views.admin_delete_laboratorio, name='admin_delete_laboratorio'),
]