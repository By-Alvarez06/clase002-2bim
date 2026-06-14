from django.db import models

# Create your models here.


class Ciclo(models.Model):
    """ """

    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()

    ciclo = models.ForeignKey(Ciclo, related_name="elciclo", on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre del estudiante: {self.nombre} {self.apellido} | {self.cedula} | Edad: {self.edad} | Ciclo: {self.ciclo}"
