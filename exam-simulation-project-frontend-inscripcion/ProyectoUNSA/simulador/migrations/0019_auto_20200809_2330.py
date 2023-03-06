# Generated by Django 3.0.6 on 2020-08-10 04:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulador', '0018_auto_20200809_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examen',
            name='Nmro_Preguntas',
            field=models.IntegerField(blank=True, default=80, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(80)]),
        ),
    ]
