#encoding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.forms import User
from .models import *

observaciones = (('PAQUETE CERRADO', 'PAQUETE CERRADO',), ('PAQUETE CERRADO Y SELLADO', 'PAQUETE CERRADO Y SELLADO',),('PAQUETE ABIERTO', 'PAQUETE ABIERTO',),('PAQUETE PERSONAL', 'PAQUETE PERSONAL',),('PAQUETE CORTADO', 'PAQUETE CORTADO',),('PAQUETE CONTAMINADO', 'PAQUETE CONTAMINADO',),('OTROS', 'OTROS',))
class FormProducto(ModelForm):
	Observaciones=forms.ChoiceField(widget=forms.Select, choices=observaciones)
	class Meta():
		model = Producto
		exclude=('estado','Usuario','Total','Cliente',)

cliente = (('CLIENTE PARTICULAR', 'CLIENTE PARTICULAR',), ('CLIENTE INSTITUCIONAL', 'CLIENTE INSTITUCIONAL',))
class FormCliente(ModelForm):
	Cliente=forms.ChoiceField(widget=forms.Select, choices=cliente)
	class Meta():
		model = Cliente
		exclude=('estado',)
class FormElemento(ModelForm):
	class Meta():
		model = Elemento
		exclude=('estado',)

class FormResultado(ModelForm):
	class Meta():
		model = Resultado
		exclude=('estado','producto',)
class FormSalida(ModelForm):
	class Meta():
		model = Salida
		exclude=('estado','Usuario',)