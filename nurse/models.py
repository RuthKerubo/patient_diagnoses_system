
from django.contrib.auth import get_user_model
from django.urls import reverse

from patient.models import Patient


from django.db import models


class Nurse(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{} <{}>".format(self.user.get_full_name(), self.user.email)

    def get_absolute_url(self):
        return reverse('nurse_detail', args=[str(self.id)])


class NursePatient(models.Model):
    nurse = models.ForeignKey(
        Nurse,
        on_delete=models.CASCADE
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{} - {}".format(self.nurse, self.patient)

    def get_absolute_url(self):
        return reverse('nursepatients_list')

# Create your models here.
