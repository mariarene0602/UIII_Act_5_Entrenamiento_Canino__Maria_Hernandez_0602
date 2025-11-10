from django.contrib import admin
from .models import Cliente, Perro, Entrenamiento

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'email', 'telefono', 'fecha_registro')
    list_filter = ('fecha_registro',)
    search_fields = ('nombre', 'email', 'telefono')

@admin.register(Perro)
class PerroAdmin(admin.ModelAdmin):
    list_display = ('id_perro', 'nombre', 'raza', 'color', 'peso', 'cliente')
    list_filter = ('raza', 'cliente')
    search_fields = ('nombre', 'raza', 'cliente__nombre')

@admin.register(Entrenamiento)
class EntrenamientoAdmin(admin.ModelAdmin):
    list_display = ('id_entrenamiento', 'nombre', 'perro', 'nivel', 'fecha_inicio', 'costo')
    list_filter = ('nivel', 'fecha_inicio', 'perro')
    search_fields = ('nombre', 'perro__nombre', 'nivel')