import zipfile
from io import BytesIO
from tempfile import NamedTemporaryFile

from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render


from .models import Empresa
from .reports import (
    crear_reporte_de_compras,
    crear_reporte_de_ventas_a_consumidor_final,
    crear_reporte_de_ventas_a_contribuyentes,
)


@login_required
@permission_required(
    (
        "contabilidad.change_compras",
        "contabilidad.change_ventasaconsumidorfinal",
        "contabilidad.change_ventasacontribuyente",
    )
)
def libros_y_reportes_mensuales_de_empresa(request, empresa_id, year, month):
    """
    Vista que retorna un zip con los siguientes PDFs:
    - Reporte de compras mensual
    - Reporte de ventas a contribuyentes
    - Reporte de ventas a consumidor final
    Que corresponden a la empresa cuyo ID se pasa y al mes y año de la fecha dada
    """
    byte_data = BytesIO()
    zip_file = zipfile.ZipFile(file=byte_data, mode="w")
    empresa = Empresa.objects.get(id=empresa_id)
    reporte_de_compras = crear_reporte_de_compras(empresa=empresa, año=year, mes=month)
    reportes_descripcion_corta = f"{empresa.nombre}_libros_y_reportes_{year}_{month}"

    with NamedTemporaryFile() as tmp:
        reporte_de_compras.output(tmp.name)
        tmp.seek(0)
        stream = tmp.read()
        zip_file.writestr(f"Compras-{reportes_descripcion_corta}.pdf", stream)

    zip_file.close()
    response = HttpResponse(byte_data.getvalue(), content_type="application/zip")
    response["Content-Disposition"] = (
        f"attachment; filename={reportes_descripcion_corta}.zip"
    )
    return response
