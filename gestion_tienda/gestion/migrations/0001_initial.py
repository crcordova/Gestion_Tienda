# Generated by Django 4.1.7 on 2023-02-28 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50, verbose_name='Sección')),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comuna', models.CharField(max_length=50, verbose_name='Comuna')),
            ],
            options={
                'ordering': ['comuna'],
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('detalle', models.TextField(blank=True, max_length=500, null=True)),
                ('categoria', models.ManyToManyField(related_name='Categoria_1', to='gestion.categorias')),
                ('categoria2', models.ManyToManyField(blank=True, related_name='Categoria_2', to='gestion.categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('web', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Región')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cliente_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cliente')),
                ('cliente_id', models.CharField(blank=True, max_length=12, null=True)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=0, max_digits=20)),
                ('entregado', models.BooleanField()),
                ('detalle', models.TextField(blank=True, max_length=500, null=True)),
                ('comuna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.comuna')),
                ('pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.pago')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.producto')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.region')),
            ],
            options={
                'ordering': ['fecha'],
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.proveedor'),
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('precio', models.DecimalField(decimal_places=3, max_digits=20)),
                ('cantidad', models.IntegerField()),
                ('tc', models.DecimalField(decimal_places=1, max_digits=20, verbose_name='Tipo de Cambio')),
                ('detalle', models.TextField(blank=True, max_length=500, null=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.producto')),
            ],
        ),
    ]
