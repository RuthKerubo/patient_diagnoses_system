from django.urls import reverse
from django.conf import settings
from patient.models import Patient

from django.db import models

from datetime import datetime


class Diagnosis(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,)
    medical_diagnosis = models.CharField(
        verbose_name='Medical Diagnosis', max_length=50)
    description = models.TextField(verbose_name='Description')
    nursing_diagnosis = models.TextField(verbose_name='Nursing Diagnosis')
    by_specialist_nurse = models.CharField(
        verbose_name='By', default="", max_length=50)

    date = models.DateTimeField(
        verbose_name=' Date (YY-MM-DD)')

    def __str__(self):
        return self.medical_diagnosis

    def get_absolute_url(self):
        return reverse('diagnosis_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Diagnosis'
        verbose_name_plural = 'Diagnoses'

# Create your models here.
