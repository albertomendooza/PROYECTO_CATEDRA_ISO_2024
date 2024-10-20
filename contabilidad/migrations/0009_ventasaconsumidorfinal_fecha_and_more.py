# Generated by Django 5.0.2 on 2024-02-25 19:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0008_rename_tipo_de_comprobate_ventasaconsumidorfinal_tipo_de_comprobante_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventasaconsumidorfinal',
            name='fecha',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='ventasaconsumidorfinal',
            name='tipo_de_venta',
            field=models.CharField(choices=[('IN', 'Interna'), ('EX', 'Exportación')], default='IN', max_length=2),
        ),
    ]
