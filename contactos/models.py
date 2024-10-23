from django.db import models


class Contacto(models.Model):
    """
    Representa a una persona natural o jurídica
    que puede ser proveedor, cliente o ambas
    """

    nombre = models.CharField(
        max_length=200, help_text="Ingrese el nombre o razón social"
    )
    tipo_de_persona = models.CharField(
        max_length=1, choices=[("N", "Persona Natural"), ("J", "Persona Jurídica")]
    )
    clasificacion = models.CharField(
        max_length=1,
        choices=(("P", "Pequeño"), ("M", "Mediano"), ("G", "Gran Contribuyente")),
        verbose_name="clasificación",
    )
    nrc = models.CharField(
        max_length=12,
        help_text="Número de registro del contribuyente",
        verbose_name="NRC",
    )
    nit = models.CharField(
        max_length=20,
        help_text="Número de Identificación tributaria",
        verbose_name="NIT",
    )
    direccion = models.CharField(
        max_length=100, verbose_name="Dirección", blank=True, null=True
    )
    telefono = models.CharField(
        max_length=100, verbose_name="Teléfono", blank=True, null=True
    )
    cliente = models.BooleanField(verbose_name="¿Cliente?", default=False)
    proveedor = models.BooleanField(verbose_name="¿Proveedor?", default=False)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.nrc}"


class ConsumidorFinal(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_de_documento = models.CharField(
        max_length=1, choices=(("D", "DUI"), ("N", "NIT"), ("O", "Otro"))
    )
    numero_de_documento = models.CharField(
        max_length=10, verbose_name="número de documento"
    )

    class Meta:
        verbose_name = "consumidor final"
        verbose_name_plural = "consumidores finales"
    
    def __str__(self) -> str:
        return f"{self.nombre} - {self.numero_de_documento}"