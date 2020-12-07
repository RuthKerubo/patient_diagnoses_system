from django.db import models

from django.conf import settings

from django.contrib.auth import get_user_model

from django.urls import reverse


class Patient(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        default='',
        on_delete=models.CASCADE

    )
   # patient_id = models.CharField(verbose_name="Patient Id", max_length=50, unique=True, default='')

    

    class Meta:
        ordering = ['user__id_no']
        
    def __str__(self):
        return self.user.id_no

    def __str__(self):
        return "{} <{}>".format(self.user.get_full_name(), self.user.email)    

    #def _str_(self):
    #   return "{} - {} {}".format(self.patient_id)

    def get_absolute_url(self):
        return reverse('patient_detail', args=[str(self.id)])


# Create your models here.
