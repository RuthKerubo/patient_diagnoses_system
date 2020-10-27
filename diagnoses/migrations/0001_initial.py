# Generated by Django 3.1.2 on 2020-10-26 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_diagnosis', models.CharField(max_length=50, verbose_name='Medical Diagnosis')),
                ('description', models.TextField(verbose_name='Description')),
                ('nursing_diagnosis', models.TextField(verbose_name='Nursing Diagnosis')),
                ('date', models.DateField(verbose_name='Date')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
            options={
                'verbose_name': 'Diagnosis',
                'verbose_name_plural': 'Diagnoses',
            },
        ),
    ]
