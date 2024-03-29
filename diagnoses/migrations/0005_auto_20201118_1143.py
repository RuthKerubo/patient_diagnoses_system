# Generated by Django 3.1.2 on 2020-11-18 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20201106_1542'),
        ('diagnoses', '0004_auto_20201113_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patient.patient'),
        ),
    ]
