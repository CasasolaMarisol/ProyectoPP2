# Generated by Django 5.0.7 on 2024-08-21 16:47

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos_Vendidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('total_venta', models.IntegerField()),
                ('metodo_pago', models.CharField(choices=[('', ''), ('Efectivo', 'Efectivo'), ('Transferencia', 'Transferencia'), ('Tarjeta_de_Debito', 'Tarjeta de Debito'), ('Tarjeta_de_Credito', 'Tarjeta de Credito')], default='', max_length=25)),
                ('id_sesion', models.CharField(max_length=100)),
                ('productos', models.ManyToManyField(through='Ventas.Productos_Vendidos', to='Productos.producto')),
            ],
        ),
        migrations.AddField(
            model_name='productos_vendidos',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ventas.venta'),
        ),
    ]
