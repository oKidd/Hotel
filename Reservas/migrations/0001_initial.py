# Generated by Django 4.1.7 on 2023-06-28 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoHabitacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados Habitacion',
            },
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False)),
                ('personas', models.IntegerField()),
                ('valor', models.IntegerField()),
                ('caracteristicas', models.CharField(max_length=200)),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Reservas.estadohabitacion')),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('adultos', models.IntegerField()),
                ('ninos', models.IntegerField()),
                ('neto', models.IntegerField()),
                ('iva', models.IntegerField()),
                ('total', models.IntegerField()),
                ('fecha_pago', models.DateField()),
                ('hora_pago', models.TimeField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('habitacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Reservas.habitacion')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
        migrations.CreateModel(
            name='TipoCama',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos Cama',
            },
        ),
        migrations.CreateModel(
            name='TipoHabitacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos Habitacion',
            },
        ),
        migrations.CreateModel(
            name='DetalleReserva',
            fields=[
                ('id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Reservas.reserva')),
                ('precio', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Detalles Reserva',
            },
        ),
        migrations.CreateModel(
            name='UserExtraInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=50, null=True)),
                ('rut', models.CharField(max_length=10, null=True)),
                ('nacimiento', models.DateField(null=True)),
                ('telefono', models.CharField(default='', max_length=30, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Info Extra Usuarios',
            },
        ),
        migrations.AddField(
            model_name='habitacion',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Reservas.tipohabitacion'),
        ),
        migrations.CreateModel(
            name='Cama',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(default=0)),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservas.habitacion')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservas.tipocama')),
            ],
            options={
                'verbose_name': 'Cama',
                'verbose_name_plural': 'Camas Habitacion',
            },
        ),
    ]
