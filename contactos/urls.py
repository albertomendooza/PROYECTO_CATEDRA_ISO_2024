from django.urls import path

from .views import json_view_compra_sujeta_a_percepcion

app_name = "contactos"
urlpatterns = [
    path(
        "json_view_compra_sujeta_a_percepcion/<int:pk_proveedor>/",
        json_view_compra_sujeta_a_percepcion,
        name="json_view_compra_sujeta_a_percepcion",
    )
]
