# Generated by Django 3.1.4 on 2020-12-07 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diagnoses', '0007_remove_diagnosis_by_specialist_nurse'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
