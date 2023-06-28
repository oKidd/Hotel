from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserExtraInfo(models.Model):
  class Meta:
      verbose_name_plural = "Info Extra Usuarios"
      verbose_name = "Usuario"

  user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
  pais = models.CharField(max_length=50, null=True)
  rut = models.CharField(max_length=10, null=True)
  nacimiento = models.DateField(null=True)
  telefono = models.CharField(max_length=30, default="", null=True)

class TipoHabitacion(models.Model):
  class Meta:
      verbose_name_plural = "Tipos Habitacion"
      verbose_name = "Tipo"

  id = models.AutoField(primary_key=True)
  tipo = models.CharField(max_length=30)
  
  def __str__(self):
      return f'{self.tipo}'

class EstadoHabitacion(models.Model):
  class Meta:
      verbose_name_plural = "Estados Habitacion"
      verbose_name = "Estado"

  id = models.AutoField(primary_key=True)
  estado = models.CharField(max_length=30)

  def __str__(self):
      return f'{self.estado}'

class Habitacion(models.Model):
  class Meta:
      verbose_name_plural = "Habitaciones"
      verbose_name = "Habitacion"

  numero = models.AutoField(primary_key=True)
  personas = models.IntegerField()
  tipo = models.ForeignKey(TipoHabitacion, null=True, blank=True, on_delete=models.CASCADE)
  estado = models.ForeignKey(EstadoHabitacion, null=True, blank=True, on_delete=models.CASCADE)
  valor = models.IntegerField()
  caracteristicas = models.CharField(max_length=200)

  def __str__(self):
      return f'Habitacion {self.numero}'
  
class TipoCama(models.Model):
  class Meta:
      verbose_name_plural = "Tipos Cama"
      verbose_name = "Tipo"

  id = models.AutoField(primary_key=True)
  tipo = models.CharField(max_length=50)
  descripcion = models.TextField()

  def __str__(self):
      return f'{self.tipo}'

class Cama(models.Model):
  class Meta:
      verbose_name_plural = "Camas Habitacion"
      verbose_name = "Cama"

  id = models.AutoField(primary_key=True)
  habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
  tipo = models.ForeignKey(TipoCama, on_delete=models.CASCADE)
  cantidad = models.IntegerField(default=0)

class Reserva(models.Model):
  class Meta:
      verbose_name_plural = "Reservas"
      verbose_name = "Reserva"

  id = models.AutoField(primary_key=True)
  usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
  habitacion = models.ForeignKey(Habitacion, null=True, blank=True, on_delete=models.CASCADE)
  adultos = models.IntegerField()
  ninos = models.IntegerField()
  neto = models.IntegerField()
  iva = models.IntegerField()
  total = models.IntegerField()
  # fecha_pago = models.DateField()
  # hora_pago = models.TimeField()
  fecha_inicio = models.DateField()
  fecha_termino = models.DateField()

class DetalleReserva(models.Model):
  class Meta:
      verbose_name_plural = "Detalles Reserva"

  id = models.ForeignKey(Reserva, primary_key=True,  null=False, blank=True, on_delete=models.CASCADE)
  precio = models.IntegerField()
