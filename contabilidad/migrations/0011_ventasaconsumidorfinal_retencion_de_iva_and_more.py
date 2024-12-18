# Generated by Django 5.0.2 on 2024-02-25 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0010_remove_ventasaconsumidorfinal_iva_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventasaconsumidorfinal',
            name='retencion_de_iva',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='IVA Retenido (-)'),
        ),
        migrations.AddField(
            model_name='ventasaconsumidorfinal',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='ventasaconsumidorfinal',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='ventasaconsumidorfinal',
            name='ventas_exentas',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='ventasaconsumidorfinal',
            name='ventas_gravadas',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='ventasaconsumidorfinal',
            name='ventas_no_sujetas',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
