from django.contrib import admin

from .models import Patient


class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = ['user']


admin.site.register(Patient, PatientAdmin)
   

# Register your models here.
