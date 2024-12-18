# Generated by Django 5.0.2 on 2024-02-24 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0003_alter_ventasaconsumidorfinal_numero_sucursal'),
        ('contactos', '0001_initial'),
        ('empresas', '0007_sucursal_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compras',
            name='nombre_de_proveedor',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='nrc_proveedor',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='numero_de_comprobante',
        ),
        migrations.RemoveField(
            model_name='ventasaconsumidorfinal',
            name='codigo_cliente',
        ),
        migrations.RemoveField(
            model_name='ventasaconsumidorfinal',
            name='nombre_de_comprobantes',
        ),
        migrations.RemoveField(
            model_name='ventasaconsumidorfinal',
            name='nombre_de_sucursal',
        ),
        migrations.RemoveField(
            model_name='ventasaconsumidorfinal',
            name='nombre_del_cliente',
        ),
        migrations.RemoveField(
            model_name='ventasaconsumidorfinal',
            name='numero_de_resolucion',
        ),
        migrations.RemoveField(
            model_name='ventasaconsumidorfinal',
            name='numero_sucursal',
        ),
        migrations.RemoveField(
            model_name='ventasacontribuyente',
            name='nombre_de_comprobantes',
        ),
        migrations.RemoveField(
            model_name='ventasacontribuyente',
            name='nombre_de_sucursal',
        ),
        migrations.RemoveField(
            model_name='ventasacontribuyente',
            name='nombre_del_cliente',
        ),
        migrations.RemoveField(
            model_name='ventasacontribuyente',
            name='nrc_cliente',
        ),
        migrations.RemoveField(
            model_name='ventasacontribuyente',
            name='numero_de_resolucion',
        ),
        migrations.RemoveField(
            model_name='ventasacontribuyente',
            name='numero_sucursal',
        ),
        migrations.AddField(
            model_name='compras',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='contactos.contacto', verbose_name='NRC de proveedor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ventasaconsumidorfinal',
            name='sucursal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresas.sucursal', verbose_name='sucursal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ventasacontribuyente',
            name='cliente',
            field=models.ForeignKey(default=1, limit_choices_to={'cliente': True}, on_delete=django.db.models.deletion.PROTECT, to='contactos.contacto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ventasacontribuyente',
            name='sucursal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresas.sucursal', verbose_name='número de sucursal'),
            preserve_default=False,
        ),
    ]
