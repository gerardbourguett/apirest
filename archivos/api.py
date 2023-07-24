from django.http import HttpResponse
from .models import Archivo, Empleado
from rest_framework import viewsets, permissions
from .serializers import ArchivoSerializer, EmpleadoSerializer


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadoSerializer


class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ArchivoSerializer


class DescargarArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ArchivoSerializer

    def get_queryset(self):
        archivo_id = self.kwargs["archivo_id"]
        return Archivo.objects.filter(pk=archivo_id)

    def retrieve(self, request, *args, **kwargs):
        archivo = self.get_object()
        # Aquí puedes hacer validaciones adicionales, por ejemplo, verificar si el usuario tiene permiso para acceder al archivo.
        # Abre el archivo en modo binario y lee su contenido.
        with open(archivo.archivo.path, "rb") as file:
            response = HttpResponse(
                file.read(), content_type="application/octet-stream"
            )
            response[
                "Content-Disposition"
            ] = f'attachment; filename="{archivo.nombre_archivo}"'
            return response
