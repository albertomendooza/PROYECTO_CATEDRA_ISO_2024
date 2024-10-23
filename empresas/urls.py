from django.urls import path

from .views import json_view_comprobante

app_name = "empresas"
urlpatterns = [
    path(
        "json_view_comprobante/<int:pk_empresa>/<int:pk_sucursal>/<str:tipo_de_comprobante>/",
        json_view_comprobante,
        name="json_view_comprobante",
    )
]
