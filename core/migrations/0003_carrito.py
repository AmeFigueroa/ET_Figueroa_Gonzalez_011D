# Generated by Django 4.1.7 on 2023-06-18 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField(verbose_name='Precio Producto')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion de Envío')),
                ('datosPay', models.CharField(max_length=50, verbose_name='Datos Pay-Pal')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto', verbose_name='Producto')),
            ],
        ),
    ]
