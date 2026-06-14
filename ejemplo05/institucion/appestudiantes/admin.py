from django.contrib import admin

# Register your models here.
from appestudiantes.models import Ciclo, Estudiante

admin.site.register(Estudiante)
admin.site.register(Ciclo)
