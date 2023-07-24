from rest_framework import routers
from .api import ArchivoViewSet, EmpleadoViewSet, DescargarArchivoViewSet
from django.conf import settings
from django.conf.urls.static import static
from . import views

router = routers.DefaultRouter()

router.register("api/empleados", EmpleadoViewSet)
router.register("api/archivos", ArchivoViewSet)
router.register("api/empleados/<int:id>/archivos", ArchivoViewSet, basename="archivos")
router.register(
    "api/archivos/<int:id>/descargar",
    DescargarArchivoViewSet,
    basename="descargar",
)

urlpatterns = router.urls
# Configuración para servir archivos de medios durante el desarrollo.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
