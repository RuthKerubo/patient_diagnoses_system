# Generated by Django 3.1.2 on 2020-11-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnoses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='date',
            field=models.DateTimeField(verbose_name=' Date (YY-MM-DD)'),
        ),
    ]
