from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse

from .models import Comprobante


@permission_required("empresa.view_comprobante")
def json_view_comprobante(request, pk_empresa, pk_sucursal, tipo_de_comprobante):
    """
    Dado el pk de un comprobante retorna la serie de documento y
    el número de resolución
    """
    try:
        comprobante = Comprobante.objects.get(
            empresa__id=pk_empresa,
            sucursal__id=pk_sucursal,
            tipo_de_comprobante=tipo_de_comprobante,
            marcar_como_actual=True,
        )
    except Comprobante.DoesNotExist:
        return JsonResponse({"serie_de_documento": "", "numero_de_resolucion": ""})
    serie_de_documento = comprobante.serie_de_documento
    numero_de_resolucion = comprobante.numero_de_resolucion
    return JsonResponse(
        {
            "serie_de_documento": serie_de_documento,
            "numero_de_resolucion": numero_de_resolucion,
        }
    )
