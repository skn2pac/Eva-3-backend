# Generated by Django 4.1.3 on 2022-11-25 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='carrera',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='email',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='ex_liceo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='fono',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]