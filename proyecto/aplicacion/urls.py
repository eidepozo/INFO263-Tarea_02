from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.principal, name='principal'),
url(r'^academico/$', views.academico, name='academico'),
url(r'^academico/nuevo/$', views.nuevo_academico, name='nuevo_academico'),
url(r'^asignatura/$', views.asignatura, name='asignatura'),
url(r'^asignatura/nuevo/$', views.nueva_asignatura, name='nueva_asignatura'),
url(r'^cargafamiliar/$', views.carga_familiar, name='carga_familiar'),

]
