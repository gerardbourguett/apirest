from rest_framework import routers
from .api import ArchivoViewSet, EmpleadoViewSet, DescargarArchivoViewSet
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

router = routers.DefaultRouter()

router.register("api/empleados", EmpleadoViewSet)
router.register("api/archivos", ArchivoViewSet)
router.register("api/empleados/<int:id>/archivos", ArchivoViewSet, basename="archivos")
router.register(
    "files/<int:id>",
    DescargarArchivoViewSet,
    basename="descargar",
)

urlpatterns = [
    path(
        "api/empleados/<int:empleado_id>/cantidad_archivos/",
        views.archivos_por_empleado,
        name="archivos_por_empleado",
    ),
    path(
        "api/empleados/<int:empleado_id>/archivos/",
        views.archivos_del_empleado,
        name="archivos_del_empleado",
    ),
] + router.urls

# Configuración para servir archivos de medios durante el desarrollo.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
