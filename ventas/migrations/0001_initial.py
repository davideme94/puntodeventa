# Generated by Django 5.1.3 on 2024-11-21 02:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfiguracionTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_negocio', models.CharField(default='Mi Negocio', max_length=100, verbose_name='Nombre del Negocio')),
                ('direccion', models.CharField(blank=True, max_length=200, verbose_name='Dirección')),
                ('telefono', models.CharField(blank=True, max_length=15, verbose_name='Teléfono')),
                ('mensaje_final', models.TextField(blank=True, default='Gracias por su compra', verbose_name='Mensaje Final')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_barra', models.CharField(max_length=50, unique=True, verbose_name='Código de Barra')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Producto')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de la Venta')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total de la Venta')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1, verbose_name='Cantidad')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Subtotal')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.producto', verbose_name='Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='ventas.venta', verbose_name='Venta')),
            ],
        ),
    ]