from django.db import models
from django.contrib.auth.models import User

# Base de datos orientada a objetos
# ORM (Object Relational Mapping)

class Marcador(models.Model):
	descripcion = models.CharField(max_length=100)
	url = models.URLField()
	fecha = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, null=True, blank=True)

	def __unicode__(self):
		return self.descripcion

