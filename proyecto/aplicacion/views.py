# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import AppAcademico
from .models import AppAsignatura
from .models import AppCargaFamiliar
from django import forms

def principal(request):
	return render(request, 'aplicacion/principal.html')

def academico(request):
	return render(request, 'aplicacion/academico.html', {'var':AppAcademico.objects.all()})

def asignatura(request):
	return render(request, 'aplicacion/asignatura.html', {'var':AppAsignatura.objects.all()})

def carga_familiar(request):
	return render(request, 'aplicacion/carga_familiar.html', {'var':AppCargaFamiliar.objects.all()})

def nuevo_academico(request):
	if(request.method=='POST'):
		form=Form_nuevo_academico(request.POST)
		if form.is_valid():
			datos=form.cleaned_data
			nuevo=AppAcademico()
			nuevo.nombre=datos.get('nombre')
			nuevo.apellido=datos.get('apellido')
			nuevo.rut=datos.get('rut')
			nuevo.save()
			return principal(request)
		else:
			return HttpResponse("datos invalidos");
	elif(request.method=='GET'):
		return render(request, 'aplicacion/nuevo_academico.html')
	else:
		return HttpResponse('metodo no soportado')

def nueva_asignatura(request):
	if(request.method=='POST'):
		form=Form_nueva_asignatura(request.POST)
		if form.is_valid():
			datos=form.cleaned_data
			nuevo=AppAsignatura()
			nuevo.nombre=datos.get('nombre')
			nuevo.codigo=datos.get('codigo')
			nuevo.save()
			return principal(request)
		else:
			return HttpResponse("datos invalidos");
	elif(request.method=='GET'):
		return render(request, 'aplicacion/nueva_asignatura.html')
	else:
		return HttpResponse('metodo no soportado')

class Form_nuevo_academico(forms.Form):
	nombre = forms.CharField(max_length=200)
	apellido = forms.CharField(max_length=200)
	rut = forms.CharField(max_length=20)

class Form_nueva_asignatura(forms.Form):
	codigo = forms.CharField(max_length=20)
	nombre = forms.CharField(max_length=30)
