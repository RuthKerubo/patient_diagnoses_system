# Generated by Django 3.1.4 on 2020-12-06 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_auto_20201206_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['id_number']},
        ),
        migrations.RemoveField(
            model_name='patient',
            name='patient_id',
        ),
        migrations.AddField(
            model_name='patient',
            name='first_name',
            field=models.CharField(default='', max_length=50, verbose_name='Firstname'),
        ),
        migrations.AddField(
            model_name='patient',
            name='id_number',
            field=models.CharField(default='', max_length=50, unique=True, verbose_name='Id Number'),
        ),
        migrations.AddField(
            model_name='patient',
            name='surname',
            field=models.CharField(default='', max_length=50, verbose_name='Surname'),
        ),
    ]
