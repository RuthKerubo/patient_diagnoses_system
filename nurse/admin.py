from django.contrib import admin

from .models import Nurse, NursePatient


class NurseAdmin(admin.ModelAdmin):
    model = Nurse
    list_display = ['user', ]


class NursePatientAdmin(admin.ModelAdmin):
    model = NursePatient
    list_display = ['nurse', 'patient', ]


admin.site.register(Nurse, NurseAdmin)
admin.site.register(NursePatient, NursePatientAdmin)

# Register your models here.
