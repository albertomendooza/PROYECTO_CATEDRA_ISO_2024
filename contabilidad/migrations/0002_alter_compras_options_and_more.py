# Generated by Django 4.2.10 on 2024-02-23 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("contactos", "0001_initial"),
        ("contabilidad", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="compras",
            options={"verbose_name": "compra", "verbose_name_plural": "compras"},
        ),
        migrations.AlterModelOptions(
            name="ventasaconsumidorfinal",
            options={
                "verbose_name": "venta a consumidor final",
                "verbose_name_plural": "ventas a consumidor final",
            },
        ),
        migrations.AlterModelOptions(
            name="ventasacontribuyente",
            options={
                "verbose_name": "venta a contribuyente",
                "verbose_name_plural": "ventas a contribuyentes",
            },
        ),
        migrations.AlterField(
            model_name="compras",
            name="nrc_proveedor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="contactos.contacto",
                verbose_name="NRC de proveedor",
            ),
        ),
    ]
