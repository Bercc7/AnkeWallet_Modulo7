from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f"{self.usuario.username} (Cliente)"

class Cuenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre_cuenta = models.CharField(max_length=50, help_text="Ej: Cuenta Corriente, Ahorros")
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_cuenta} - ${self.saldo}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    TIPO_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('egreso', 'Egreso'),
    ]
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(Categoria, blank=True)

    def __str__(self):
        return f"{self.tipo.capitalize()} - ${self.monto} ({self.descripcion})"