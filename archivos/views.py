from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Archivo, Empleado
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArchivoSerializer


@api_view(["GET"])
def archivos_del_empleado(request, empleado_id):
    try:
        empleado = Empleado.objects.get(pk=empleado_id)
        archivos = empleado.archivos.all()
        serializer = ArchivoSerializer(archivos, many=True)
        return Response(serializer.data)
    except Empleado.DoesNotExist:
        return Response({"error": "El empleado no existe."}, status=404)


@api_view(["GET"])
def archivos_por_empleado(request, empleado_id):
    try:
        empleado = Empleado.objects.get(pk=empleado_id)
        cantidad_archivos = empleado.archivos.count()
        return Response(
            {"empleado_id": empleado_id, "cantidad_archivos": cantidad_archivos}
        )
    except Empleado.DoesNotExist:
        return Response({"error": "El empleado no existe."}, status=404)


def serve_file(request, archivo_id):
    archivo = get_object_or_404(Archivo, pk=archivo_id)

    # Aquí puedes hacer validaciones adicionales, por ejemplo, verificar si el usuario tiene permiso para acceder al archivo.

    # Abre el archivo en modo binario y lee su contenido.
    with open(archivo.archivo.path, "rb") as file:
        response = HttpResponse(file.read(), content_type="application/octet-stream")
        response[
            "Content-Disposition"
        ] = f'attachment; filename="{archivo.nombre_archivo}"'
        return response
