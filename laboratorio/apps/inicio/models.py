from django.db import models
from django.contrib.auth.forms import User
# Create your models here.
class Perfiles(models.Model):
	usuario = models.OneToOneField(User, unique=True, related_name='perfil')
	ci = models.IntegerField(max_length=10)
	#telefono = models.IntegerField(max_length=8)
	def __unicode__(self):
		return self.usuario.username