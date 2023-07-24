from rest_framework import serializers
from .models import Archivo, Empleado


class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo
        fields = ("id", "nombre_archivo", "descripcion", "archivo", "fecha", "empleado")
        read_only_fields = ("id", "fecha")


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ("id", "nombre_completo", "fecha_creacion", "fecha_modificacion")
        read_only_fields = ("id", "fecha_creacion", "fecha_modificacion")
