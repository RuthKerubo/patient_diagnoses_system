# Generated by Django 3.1.2 on 2020-11-03 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
        ('diagnoses', '0002_auto_20201103_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='patient',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
    ]
