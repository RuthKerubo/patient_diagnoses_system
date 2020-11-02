
from django.contrib.auth import get_user_model
from django.urls import reverse

from patient.models import Patient


from django.db import models


class Specialist(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{} <{}>".format(self.user.get_full_name(), self.user.email)

    def get_absolute_url(self):
        return reverse('specialist_detail', args=[str(self.id)])


class SpecialistPatient(models.Model):
    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.CASCADE
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{} - {}".format(self.specialist, self.patient)

    def get_absolute_url(self):
        return reverse('specialistpatients_list')


# Create your models here.
