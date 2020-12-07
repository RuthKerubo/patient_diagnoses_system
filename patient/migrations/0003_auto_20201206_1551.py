# Generated by Django 3.1.4 on 2020-12-06 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0002_auto_20201106_1542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['patient_id']},
        ),
        migrations.RemoveField(
            model_name='patient',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='id_number',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='surname',
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_id',
            field=models.CharField(default='', max_length=50, unique=True, verbose_name='Patient Id'),
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
