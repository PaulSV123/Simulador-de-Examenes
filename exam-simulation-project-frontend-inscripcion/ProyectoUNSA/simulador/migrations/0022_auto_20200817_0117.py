# Generated by Django 2.1.15 on 2020-08-17 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulador', '0021_auto_20200812_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examen',
            name='Estado',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
