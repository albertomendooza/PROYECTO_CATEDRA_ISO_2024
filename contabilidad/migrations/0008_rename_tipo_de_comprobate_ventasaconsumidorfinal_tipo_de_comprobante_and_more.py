# Generated by Django 5.0.2 on 2024-02-25 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0007_remove_ventasacontribuyente_venta_excenta_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ventasaconsumidorfinal',
            old_name='tipo_de_comprobate',
            new_name='tipo_de_comprobante',
        ),
        migrations.RenameField(
            model_name='ventasacontribuyente',
            old_name='tipo_de_comprobate',
            new_name='tipo_de_comprobante',
        ),
        migrations.AlterField(
            model_name='ventasacontribuyente',
            name='retencion_de_iva',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='IVA Retenido (-)'),
        ),
    ]
