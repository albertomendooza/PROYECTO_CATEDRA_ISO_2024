from django.db import models

from contactos.models import Contacto
from empresas.models import Empresa, Sucursal


class Compras(models.Model):
    empresa = models.ForeignKey(to=Empresa, on_delete=models.PROTECT)
    nrc_proveedor = models.ForeignKey(to=Contacto, on_delete=models.PROTECT, verbose_name="NRC de proveedor")
    nombre_de_proveedor = models.CharField(max_length=200)
    tipo_de_comprobante = models.CharField(
        max_length=3,
        choices=(
            ("CCF", "Comprobante de Crédito Fiscal"),
            ("EXP", "Exportación"),
            ("PLZ", "Poliza"),
            ("NDC", "Nota de Crédito"),
        ),
    )
    numero_de_comprobante = models.CharField(
        max_length=32, verbose_name="número de comprobante"
    )
    numero_de_serie = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateField()
    tipo_de_compra = models.CharField(
        max_length=3, choices=(("INT", "Interna"), ("IMP", "Importación"))
    )
    compra_neta = models.DecimalField(max_digits=8, decimal_places=2)
    iva = models.DecimalField(verbose_name="I.V.A.", max_digits=8, decimal_places=2)
    percepcion_iva = models.DecimalField(
        verbose_name="percepción I.V.A.", max_digits=8, decimal_places=2
    )
    sub_total = models.DecimalField(max_digits=8, decimal_places=2)
    compra_excenta = models.DecimalField(max_digits=8, decimal_places=2)
    compra_excluida = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    tipo_de_gasto = models.CharField(
        max_length=3,
        choices=(
            ("CST", "Costo"),
            ("GAD", "Gasto de Administración"),
            ("GAV", "Gasto de Venta"),
            ("GAF", "Gasto Financiero"),
            ("OGA", "Otro Gasto"),
        ),
    )

    class Meta:
        verbose_name = "compra"
        verbose_name_plural = "compras"


class VentasAConsumidorFinal(models.Model):
    empresa = models.ForeignKey(to=Empresa, on_delete=models.PROTECT)
    numero_sucursal = models.ForeignKey(
        to=Sucursal, verbose_name="número de sucursal", on_delete=models.PROTECT
    )
    nombre_de_sucursal = models.CharField(max_length=100)
    tipo_de_comprobate = models.CharField(
        max_length=3,
        choices=(
            ("FAC", "Factura de Consumidor Final"),
            ("NDC", "Nota de Crédito"),
        ),
    )
    nombre_de_comprobantes = models.CharField(max_length=100)
    numero_de_resolucion = models.CharField(max_length=30)
    serie_de_documento = models.CharField(max_length=30)
    codigo_cliente = models.ForeignKey(
        to=Contacto, limit_choices_to={"cliente": True}, on_delete=models.PROTECT
    )
    nombre_del_cliente = models.CharField(max_length=200)
    numero_de_documento = models.CharField(
        max_length=35, verbose_name="número de documento"
    )
    tipo_de_venta = models.CharField(
        max_length=2, choices=(("IN", "Interna"), ("EX", "Exportación"))
    )
    total_venta_gravada = models.DecimalField(max_digits=8, decimal_places=2)
    venta_neta = models.DecimalField(max_digits=8, decimal_places=2)
    iva = models.DecimalField(verbose_name="IVA", max_digits=8, decimal_places=2)
    sub_total = models.DecimalField(max_digits=8, decimal_places=2)
    retencion_de_iva = models.DecimalField(max_digits=8, decimal_places=2)
    total_venta_excenta = models.DecimalField(max_digits=8, decimal_places=2)
    total_general = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "venta a consumidor final"
        verbose_name_plural = "ventas a consumidor final"

    def __str__(self) -> str:
        return f"{self.empresa} - {self.numero}"
    


class VentasAContribuyente(models.Model):
    """
    Ventas a contribuyentes
    """

    empresa = models.ForeignKey(to=Empresa, on_delete=models.PROTECT)
    numero_sucursal = models.ForeignKey(
        to=Sucursal, verbose_name="número de sucursal", on_delete=models.PROTECT
    )
    nombre_de_sucursal = models.CharField(max_length=100)
    tipo_de_comprobate = models.CharField(
        max_length=3,
        choices=(("CCF", "Comprobante de Crédito Fiscal"), ("NDC", "Nota de Crédito")),
    )
    nombre_de_comprobantes = models.CharField(max_length=100)
    numero_de_resolucion = models.CharField(max_length=30)
    serie_de_documento = models.CharField(max_length=30)
    nrc_cliente = models.ForeignKey(
        to=Contacto, limit_choices_to={"cliente": True}, on_delete=models.PROTECT
    )
    nombre_del_cliente = models.CharField(max_length=200)
    numero_de_documento = models.CharField(
        max_length=35, verbose_name="número de comprobante"
    )
    venta_neta = models.DecimalField(max_digits=8, decimal_places=2)
    iva = models.DecimalField(verbose_name="IVA", max_digits=8, decimal_places=2)
    sub_total = models.DecimalField(max_digits=8, decimal_places=2)
    retencion_de_iva = models.DecimalField(max_digits=8, decimal_places=2)
    sub_total = models.DecimalField(max_digits=8, decimal_places=2)
    venta_excenta = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "venta a contribuyente"
        verbose_name_plural = "ventas a contribuyentes"

    def __str__(self) -> str:
        return f"{self.empresa} - {self.numero}"
