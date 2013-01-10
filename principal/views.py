# Create your views here.
from principal.models import Alumno, Profesor, Curso, Matricula, Dictar, Nota
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect 
from django.template import RequestContext

def lista_alumnos(request):
	alumnos = Alumno.objects.all()
	return render_to_response('lista_alumnos.html',{'alumnos':alumnos},context_instance = RequestContext(request))

def lista_cursos(request):
	cursos = Curso.objects.all()
	return render_to_response('lista_cursos.html',{'cursos':cursos},context_instance = RequestContext(request))

def lista_profesores(request):
	profesores = Profesor.objects.all()
	return render_to_response('lista_profesores.html',{'profesores':profesores},context_instance = RequestContext(request))

def dato_alumno(request, id_alumno):	
	dato = Alumno.objects.get(pk=id_alumno)
	dato2 = Matricula.objects.filter(alumno=id_alumno)
	return render_to_response('dato_alumno.html',{'alumno':dato,'cursos_matriculados':dato2},context_instance = RequestContext(request))

def dato_curso(request, id_curso):
	dato = Curso.objects.get(pk=id_curso)
	dato2 = Matricula.objects.filter(curso=id_curso)
	return render_to_response('dato_curso.html',{'curso':dato,'alumnos_matriculados':dato2},context_instance = RequestContext(request))

def dato_profesor(request,id_profesor):
	dato = Profesor.objects.get(pk =id_profesor)
	dato2 = Dictar.objects.filter(profesor= id_profesor)
	return render_to_response('dato_profesor.html',{'profesor':dato,'cursos_dictados':dato2},context_instance = RequestContext(request))
