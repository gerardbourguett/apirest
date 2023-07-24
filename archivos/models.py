from django.db import models


# Create your models here.
class Empleado(models.Model):
    nombre_completo = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_completo


class Archivo(models.Model):
    nombre_archivo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    archivo = models.FileField(upload_to="files/")
    fecha = models.DateTimeField(auto_now_add=True)

    empleado = models.ForeignKey(
        Empleado, on_delete=models.CASCADE, related_name="archivos"
    )

    def __str__(self):
        return self.nombre_archivo
