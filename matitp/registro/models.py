from django.db import models
from django.conf import settings
# Create your models here.

#Clase Alumno con los atributos normales 
class Alumno(models.Model):
	nombre = models.CharField("Nombre", max_length=30)
	apellido = models.CharField("Apellido", max_length=30)
	dni = models.PositiveIntegerField("DNI")

	class Meta:
		verbose_name = "Alumno"
		verbose_name_plural = "Alumnos"

	def __str__(self):
		return "{} {}".format(self.nombre, self.apellido)


#Clase Asignatura con los  atributos de una materia cualquiera
class Asignatura(models.Model):
	materia = models.CharField("Materia", max_length=60)
	profesor = models.CharField("Profesor/a", max_length=60)
	horario = models.PositiveIntegerField("Horario")

	class Meta:
		verbose_name = "Asignatura"
		verbose_name_plural = "Asignaturas"


	def __str__(self):
		return "{}".format(self.materia)


#Clase Matricula forkeado hacia alumno y su asignatura
class Matricula(models.Model):
	alumno = models.ForeignKey(Alumno, related_name = "asignaturas", on_delete=models.CASCADE)
	asignatura = models.ForeignKey(Asignatura, related_name= "alumnos", on_delete=models.CASCADE)

	class Meta: 
		verbose_name = "Matricula"
		verbose_name_plural = "Matriculas"

	
		#promedio suma entre las notas total llevadas hacia un valor total
	def promedio(self):
		suma = 0
		total = self.notas.count()
		if total <= 0:
			return 0
		for nota in self.notas.all():
			suma += nota.valor
		return float(suma)/total


	def __str__(self):
		return "{} {} {}".format(self.alumno, self.asignatura, self.promedio())

#Clase nota forkeada a la matricula y el valor de la nota
class Nota(models.Model):
	matricula =  models.ForeignKey(Matricula, related_name = "notas", on_delete=models.CASCADE)
	valor = models.PositiveIntegerField("Valor")

	class Meta:
		verbose_name = "Nota"
		verbose_name_plural = "Notas"

	def __str__(self):
		return "{} {} = {}".format(self.matricula.asignatura, self.matricula.alumno, self.valor)
