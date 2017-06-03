# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AppAcademico(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    rut = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'app_academico'


class AppAcademicoAsignatura(models.Model):
    id_app_academico = models.ForeignKey(AppAcademico, models.DO_NOTHING, db_column='id_app_academico', primary_key=True)
    id_app_asignatura = models.ForeignKey('AppAsignatura', models.DO_NOTHING, db_column='id_app_asignatura')

    class Meta:
        managed = False
        db_table = 'app_academico_asignatura'
        unique_together = (('id_app_academico', 'id_app_asignatura'),)


class AppAsignatura(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'app_asignatura'


class AppCargaFamiliar(models.Model):
    id = models.AutoField(primary_key=True)
    id_app_academico = models.ForeignKey(AppAcademico, models.DO_NOTHING, db_column='id_app_academico')
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    rut = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'app_carga_familiar'

    class Meta:
        managed = False
        db_table = 'app_carga_familiar'
