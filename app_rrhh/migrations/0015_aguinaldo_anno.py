# Generated by Django 4.1 on 2022-08-20 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_rrhh', '0014_aguinaldo'),
    ]

    operations = [
        migrations.AddField(
            model_name='aguinaldo',
            name='anno',
            field=models.IntegerField(default=0),
        ),
    ]
