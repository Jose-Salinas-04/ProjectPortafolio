# Generated by Django 5.0.6 on 2024-06-26 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barbero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=250)),
                ('valorizacion', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Localizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCorte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Barberia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('valorizacion', models.DecimalField(decimal_places=1, max_digits=2)),
                ('barbero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.barbero')),
            ],
        ),
        migrations.CreateModel(
            name='HorarioTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.IntegerField()),
                ('horario_inicio', models.TimeField()),
                ('horario_fin', models.TimeField()),
                ('barbero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.barbero')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.comentario')),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField()),
                ('duracion', models.DurationField()),
                ('barbero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.barbero')),
                ('tipo_corte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tipocorte')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usuario')),
            ],
        ),
    ]
