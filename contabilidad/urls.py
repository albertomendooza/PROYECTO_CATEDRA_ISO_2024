from django.urls import path

from .views import libros_y_reportes_mensuales_de_empresa

app_name = "contabilidad"
urlpatterns = [
    path(
        route="libros_y_reportes_mensuales_de_empresa/<int:empresa_id>/<int:year>/<int:month>/",
        view=libros_y_reportes_mensuales_de_empresa,
        name="libros_y_reportes_mensuales_de_empresa")
]