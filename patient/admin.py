from django.contrib import admin

from .models import Patient


class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = ['first_name', 'surname', 'id_number', ]


admin.site.register(Patient, PatientAdmin)
# Register your models here.
