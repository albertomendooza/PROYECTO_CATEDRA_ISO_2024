# Generated by Django 4.2.10 on 2024-03-13 21:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contabilidad", "0020_alter_compras_compra_excenta_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="compras",
            name="numero_de_comprobante",
            field=models.CharField(default="", max_length=32),
        ),
    ]