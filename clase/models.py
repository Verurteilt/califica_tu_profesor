from django.db import models
from users.models import User



class Clase(models.Model):
	profesor = models.ForeignKey(User)
	empieza = models.DateTimeField()
	termina = models.DateTimeField()


class ClaseAlumno(models.Model):
	alumno =	 models.ForeignKey(User)
	calificacion = models.IntegerField()
	comentario = models.TextField()
	clase = models.ForeignKey(Clase)

	class Meta:
		unique_together = ('alumno', 'clase')

