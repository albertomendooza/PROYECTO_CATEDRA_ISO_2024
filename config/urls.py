from django.urls import include, path

from contabilidad.admin import custom_admin_site

urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path("empresas/", include("empresas.urls")),
    path("contactos/", include("contactos.urls")),
    path("contabilidad/", include("contabilidad.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]
