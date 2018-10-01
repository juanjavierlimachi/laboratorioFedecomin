#encoding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Perfiles
from django.contrib.auth.forms import User
class UserForm(UserCreationForm):
	username = forms.CharField(max_length=40,required=True,label="Nombre de Usuario")
	password1 = forms.CharField(required=True,label="Contraseña",widget=forms.PasswordInput(render_value=False))
	password2 = forms.CharField(required=True, label="Confirmacion",widget=forms.PasswordInput(render_value=False))
	first_name = forms.CharField(max_length=40,required=True, label="Nombre Completo")
	last_name = forms.CharField(max_length=50,required=True, label="Apellido(s)")
	ci = forms.IntegerField(required=True,label="Nro. de CI")
	#telefono = forms.IntegerField(required=True,label="Celular")
	def clean_ci(self):
		ci=self.cleaned_data['ci']
		try:
			p=Perfiles.objects.get(ci=ci)
		except Perfiles.DoesNotExist:
			return ci
		raise forms.ValidationError('El Nro de CI ya Existe')
	class Meta:
		model=User
		fields=("username","password1","password2","first_name","last_name")
		widgets = {
			'password1':forms.PasswordInput(),
		}
	def save(self,commit=True):
		user=super(UserForm,self).save(commit=False)
		user.first_name=self.cleaned_data.get("first_name")
		user.last_name=self.cleaned_data.get("last_name")
		if commit:
			user.save()
		return user
#formularios para editar el usuario
class formPerfiles(forms.ModelForm):
	class Meta:
		model=Perfiles
		exclude=['usuario']
class UserForms(forms.ModelForm):
	class Meta:
		model=User
		fields = ('username','first_name','last_name')
		#exclude=['password']

class CambioForm(forms.Form):
	Nueva_Contracenia= forms.CharField(required=True, label="Contracenia",widget=forms.PasswordInput(render_value=False))
	Confirmacion	 = forms.CharField(required=True, label="Confirmar",widget=forms.PasswordInput(render_value=False))
	def password(self):
		pass_one=self.cleaned_data['Nueva_Contracenia']
		pass_tho=self.cleaned_data['Confirmacion']
		if pass_one == pass_tho:
			pass
		else:
			raise forms.ValidationError('Los datos no Coinsiden')