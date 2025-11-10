from django.db import models

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    fecha_registro = models.DateField()
    fecha_nacimiento = models.DateField()
    comentarios = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: PERRO
# ==========================================
class Perro(models.Model):
    id_perro = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='perros')
    # Relación 1 a muchos: un cliente puede tener varios perros

    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    color = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.raza})"

# ==========================================
# MODELO: Entrenamientos
# ==========================================
class Entrenamiento(models.Model):
    id_entrenamiento = models.AutoField(primary_key=True)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE, related_name='entrenamientos')
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    duracion_horas = models.DecimalField(max_digits=4, decimal_places=2)
    lugar = models.CharField(max_length=200)
    nivel = models.CharField(max_length=50)
    costo = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} – {self.perro.nombre}"