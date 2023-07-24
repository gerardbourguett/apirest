from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Archivo


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
