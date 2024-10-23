from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse

from .models import Contacto


@permission_required("contactos:view_contacto")
def json_view_compra_sujeta_a_percepcion(resquest, pk_proveedor):
    """
    Dado el id de una empresa y de un proveedor retorna true si la empresa
    es gran contribuyente y por tanto la compra estará sujeta a percepción
    """
    clasificacion = Contacto.objects.get(id=pk_proveedor).clasificacion
    return JsonResponse(
        {"gran_contribuyente": (True if clasificacion == "G" else False)}
    )
