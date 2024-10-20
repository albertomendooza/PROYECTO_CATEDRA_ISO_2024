from django.db import models
from django.utils import timezone

from contactos.models import Contacto, ConsumidorFinal
from empresas.models import Empresa, Sucursal


class Compras(models.Model):
    empresa = models.ForeignKey(
        to=Empresa, on_delete=models.PROTECT
    )
    proveedor = models.ForeignKey(
        to=Contacto, on_delete=models.PROTECT, limit_choices_to={"proveedor": True}
    )
    tipo_de_comprobante = models.CharField(
        max_length=3,
        choices=(
            ("CCF", "Comprobante de Crédito Fiscal"),
            ("EXP", "Exportación"),
            ("PLZ", "Poliza"),
            ("NDC", "Nota de Crédito"),
        ),
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
    sucursal = models.ForeignKey(
        to=Sucursal, verbose_name="sucursal", on_delete=models.PROTECT
    )
    tipo_de_comprobante = models.CharField(
        max_length=3,
        choices=(
            ("FAC", "Factura de Consumidor Final"),
            ("NDC", "Nota de Crédito"),
        ),
    )
    fecha = models.DateField(default=timezone.now().today)
    serie_de_documento = models.CharField(max_length=30)
    numero_de_documento = models.CharField(
        max_length=35, verbose_name="número de documento"
    )
    cliente = models.ForeignKey(to=ConsumidorFinal, on_delete=models.PROTECT)
    tipo_de_venta = models.CharField(
        max_length=2, choices=(("IN", "Interna"), ("EX", "Exportación")),
        default="IN"
    ) 
    ventas_gravadas = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    ventas_no_sujetas = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    ventas_exentas = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    sub_total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    retencion_de_iva = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="IVA Retenido (-)")
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)

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
    sucursal = models.ForeignKey(
        to=Sucursal, on_delete=models.PROTECT
    )
    fecha = models.DateField(default=timezone.now().today)
    tipo_de_comprobante = models.CharField(
        max_length=3,
        choices=(("CCF", "Comprobante de Crédito Fiscal"), ("NDC", "Nota de Crédito")),
    )
    serie_de_documento = models.CharField(max_length=30)
    cliente = models.ForeignKey(
        to=Contacto, limit_choices_to={"cliente": True}, on_delete=models.PROTECT
    )
    numero_de_documento = models.CharField(
        max_length=35, verbose_name="número de comprobante"
    )
    ventas_gravadas = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    ventas_no_sujetas = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    ventas_exentas = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    iva = models.DecimalField(verbose_name="IVA", max_digits=8, decimal_places=2)
    sub_total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    retencion_de_iva = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="IVA Retenido (-)")
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        verbose_name = "venta a contribuyente"
        verbose_name_plural = "ventas a contribuyentes"

    def __str__(self) -> str:
        return f"{self.empresa} - {self.numero_de_documento}"
