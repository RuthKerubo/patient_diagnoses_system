from django.contrib import admin

from .models import Specialist, SpecialistPatient


class SpecialistAdmin(admin.ModelAdmin):
    model = Specialist
    list_display = ['user', ]


class SpecialistPatientAdmin(admin.ModelAdmin):
    model = SpecialistPatient
    list_display = ['specialist', 'patient', ]


admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(SpecialistPatient, SpecialistPatientAdmin)

# Register your models here.
