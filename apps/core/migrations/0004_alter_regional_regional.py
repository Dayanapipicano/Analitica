# Generated by Django 5.0.5 on 2024-09-10 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_centro_de_formacion_centro_de_formacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regional',
            name='regional',
            field=models.CharField(max_length=150),
        ),
    ]
