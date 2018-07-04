# Generated by Django 2.0.6 on 2018-07-04 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('dni', models.PositiveIntegerField(verbose_name='DNI')),
            ],
            options={
                'verbose_name_plural': 'Alumnos',
                'verbose_name': 'Alumno',
            },
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=60, verbose_name='Materia')),
                ('profesor', models.CharField(max_length=60, verbose_name='Profesor/a')),
                ('horario', models.PositiveIntegerField(verbose_name='Horario')),
            ],
            options={
                'verbose_name_plural': 'Asignaturas',
                'verbose_name': 'Asignatura',
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignaturas', to='registro.Alumno')),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumnos', to='registro.Asignatura')),
            ],
            options={
                'verbose_name_plural': 'Matriculas',
                'verbose_name': 'Matricula',
            },
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.PositiveIntegerField(verbose_name='Valor')),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='registro.Matricula')),
            ],
            options={
                'verbose_name_plural': 'Notas',
                'verbose_name': 'Nota',
            },
        ),
    ]