# Generated by Django 3.0.6 on 2020-08-10 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simulador', '0014_examen_postulante_solucionario_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examen_postulante',
            name='Solucionario_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='simulador.Solucionario'),
        ),
    ]