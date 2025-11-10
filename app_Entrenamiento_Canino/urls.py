from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_entrenamiento_canino, name='inicio'),
    
    # URLs para Clientes
    path('agregar-cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('ver-cliente/', views.ver_cliente, name='ver_cliente'),
    path('actualizar-cliente/<int:id_cliente>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('realizar-actualizacion-cliente/<int:id_cliente>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('borrar-cliente/<int:id_cliente>/', views.borrar_cliente, name='borrar_cliente'),
    
    # URLs para Perros
    path('agregar-perro/', views.agregar_perro, name='agregar_perro'),
    path('ver-perro/', views.ver_perro, name='ver_perro'),
    path('actualizar-perro/<int:id_perro>/', views.actualizar_perro, name='actualizar_perro'),
    path('realizar-actualizacion-perro/<int:id_perro>/', views.realizar_actualizacion_perro, name='realizar_actualizacion_perro'),
    path('borrar-perro/<int:id_perro>/', views.borrar_perro, name='borrar_perro'),
    
    # URLs para Entrenamientos
    path('agregar-entrenamiento/', views.agregar_entrenamiento, name='agregar_entrenamiento'),
    path('ver-entrenamiento/', views.ver_entrenamiento, name='ver_entrenamiento'),
    path('actualizar-entrenamiento/<int:id_entrenamiento>/', views.actualizar_entrenamiento, name='actualizar_entrenamiento'),
    path('realizar-actualizacion-entrenamiento/<int:id_entrenamiento>/', views.realizar_actualizacion_entrenamiento, name='realizar_actualizacion_entrenamiento'),
    path('borrar-entrenamiento/<int:id_entrenamiento>/', views.borrar_entrenamiento, name='borrar_entrenamiento'),
]