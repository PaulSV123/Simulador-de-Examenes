# Generated by Django 2.1.15 on 2020-08-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulador', '0011_examen_postulante_esta_inscrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='examen',
            name='Tipo',
            field=models.CharField(choices=[('O', 'Ordinario'), ('C', 'CEPRUNSA'), ('E', 'Extraordinario')], default='O', max_length=100),
        ),
    ]
