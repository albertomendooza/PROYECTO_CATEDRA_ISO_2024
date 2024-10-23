from django.db import models


class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    nrc = models.CharField(
        max_length=10,
        verbose_name="NRC",
        help_text="Número de regisctro de contribuyente",
        unique=True,
    )
    nit = models.CharField(
        max_length=20,
        verbose_name="NIT",
        help_text="Número de identificación tributario",
        unique=True,
    )

    class Meta:
        verbose_name = " Empresa"
        verbose_name_plural = " Empresas"

    def __str__(self) -> str:
        return f"{self.nombre} - {self.nrc}"


class Sucursal(models.Model):
    empresa = models.ForeignKey(to=Empresa, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=10, verbose_name="código")

    class Meta:
        verbose_name = " Sucursal"
        verbose_name_plural = " Sucursales"

    def __str__(self) -> str:
        return f"{self.nombre} - {self.codigo}"


class Comprobante(models.Model):
    empresa = models.ForeignKey(to=Empresa, on_delete=models.PROTECT)
    sucursal = models.ForeignKey(to=Sucursal, on_delete=models.PROTECT)
    tipo_de_comprobante = models.CharField(
        max_length=3,
        choices=(
            ("FCF", "Factura de consumidor final"),
            ("CCF", "Comprobante de crédito fiscal"),
            ("NDC", "Nota de crédito"),
            ("PLZ", "Poliza"),
            ("FEX", "Factura de exportación"),
        ),
    )
    numero_de_resolucion = models.CharField(
        max_length=20, verbose_name="número de resolución"
    )
    serie_de_documento = models.CharField(
        max_length=20,
    )
    marcar_como_actual = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.numero_de_resolucion} - {self.serie_de_documento}" 
