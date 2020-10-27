from django.db import models

from django.conf import settings

from django.contrib.auth import get_user_model

from django.urls import reverse


class Patient(models.Model):
    first_name = models.CharField(verbose_name="Firstname", max_length=50)
    surname = models.CharField(verbose_name="Surname", max_length=50)
    id_number = models.CharField(
        verbose_name="Id Number", max_length=50, unique=True)

    def _str_(self):
        return "{} - {} {}".format(self.id_number, self.first_name, self.surname)

    def get_absolute_url(self):
        return reverse('patient_detail', args=[str(self.id)])
# Create your models here.
