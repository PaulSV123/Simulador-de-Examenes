# Generated by Django 3.0.6 on 2020-08-10 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulador', '0017_auto_20200809_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solucionario',
            name='respuestas',
            field=models.TextField(blank=True, default='011111111111111111111111111111111111111111111111111111111111111111111111111111111'),
        ),
    ]
