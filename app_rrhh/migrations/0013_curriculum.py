# Generated by Django 4.1 on 2022-08-19 19:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_rrhh', '0012_vacacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=15)),
                ('sexo', models.CharField(max_length=1)),
                ('fecha_nacimiento', models.DateField(default=datetime.date.today)),
                ('domicilio', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('nombre_del_cargo', models.CharField(max_length=100)),
                ('experiencia_laboral', models.TextField()),
                ('nivel_de_estudios', models.TextField()),
                ('otros_datos_interes', models.TextField(blank=True)),
                ('tiene_auto_propio', models.CharField(blank=True, max_length=2)),
                ('pdf_con_curriculum', models.FileField(blank=True, upload_to='curriculums/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]