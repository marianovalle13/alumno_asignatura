from django.shortcuts import render
from .models import *
# Create your views here.

def traer_todo(request):
	getAll_alumnos = Alumno.objects.all()
	getAll_asignaturas = Asignatura.objects.all()
	return render(request, 'home.html',{"alumnos": getAll_alumnos, "asignaturas": getAll_asignaturas})


def alumno(request):
	getAll_matricula = Matricula.objects.all()
	return render(request, 'alumno.html',{"matricula": getAll_matricula})