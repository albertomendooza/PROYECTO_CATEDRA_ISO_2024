from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class GenerarLibrosYReportesMensualesDeEmpresaForm(forms.Form):
    """
    Formulario para generar los libros y reportes de una
    empresa, se solicita unicamente la fecha a
    """

    mes = forms.IntegerField(
        help_text="Ingrese el mes en formato de dígito entre 1 y 12",
        label="Mes",
        validators=[
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=12),
        ],
    )
    año = forms.IntegerField(
        help_text="Ingrese el año en formato de 4 dígito entre 2023 y 2050",
        label="Año",
        validators=[MinValueValidator(2024), MaxValueValidator(2050)],
    )
