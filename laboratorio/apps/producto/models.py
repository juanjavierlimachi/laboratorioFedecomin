from django.db import models
from django.contrib.auth.forms import User
class Cliente(models.Model):
	Cliente=models.CharField(max_length=150)
	Nombre=models.CharField(max_length=150)
	Apellidos=models.CharField(max_length=150,blank=True,null=True)
	Ci_Nit=models.PositiveIntegerField(max_length=20, blank=True, null=True)
	Celular = models.PositiveIntegerField(max_length=8, blank=True, null=True)
	estado=models.BooleanField(default=True)
	fecha_registro = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.Nombre

class Elemento(models.Model):
	Nombre_del_Elemento = models.CharField(max_length=100)
	Abreviatura = models.CharField(max_length=100)
	estado=models.BooleanField(default=True)
	fecha_registro = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.Nombre_del_Elemento

class Producto(models.Model):
	Nro_de_Lote = models.CharField(max_length=150)
	Precio = models.PositiveIntegerField(max_length=8)
	Cantidad = models.PositiveIntegerField(max_length=8,default=1)
	Total = models.PositiveIntegerField(max_length=8)
	Observaciones = models.CharField(max_length=150)
	Cliente = models.ForeignKey(Cliente)
	Elemento = models.ForeignKey(Elemento)
	Procedencia = models.CharField(max_length=200,blank=True,null=True)
	Ficha = models.PositiveIntegerField(max_length=8)
	Usuario=models.ForeignKey(User)
	estado=models.BooleanField(default=True)
	fecha_registro = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.Nro_de_Lote

class Resultado(models.Model):
	Resultado=models.FloatField()
	Elemento=models.CharField(max_length=100)
	Abreviatura=models.CharField(max_length=100)
	producto=models.ForeignKey(Producto)
	estado=models.BooleanField(default=True)
	fecha_registro = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.producto.Nro_de_Lote

class Salida(models.Model):
	Detalle=models.TextField(max_length=200)
	Monto=models.PositiveIntegerField()
	Observaciones=models.CharField(max_length=150,blank=True,null=True)
	fecha_registro=models.DateTimeField(auto_now=True)
	Usuario=models.ForeignKey(User)
	estado=models.BooleanField(default=True)
	def __unicode__(self):
		return self.Detalle


