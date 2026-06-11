from django.db import models
import datetime

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()


    def __str__(self):
        return (f"Nombre: {self.nombre} - Apellido: {self.apellido} "
                f"- Edad: {self.edad} - Año de nacimiento: {self.obtener_anio_nacimiento()} "
                f"- Ciudad: {self.obtener_ciudad()}")
    
    def obtener_anio_nacimiento(self):
        # Obtener el año actual con Datetime
        anio_actual = datetime.date.today().year
        return anio_actual - self.edad
    
    def obtener_ciudad(self):
        # Si la cedula empieza con 11, es de Loja, sino es de 'Otra ciudad'
        if self.cedula.startswith('11'):
            return 'Loja'
        else:
            return 'Otra ciudad'