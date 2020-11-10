from django.contrib import admin
from .models import Diagnosis


class DiagnosisAdmin(admin.ModelAdmin):
    model = Diagnosis
    list_display = ['medical_diagnosis', 'description',
                    'nursing_diagnosis', 'date', 'by_specialist_nurse', ]


admin.site.register(Diagnosis, DiagnosisAdmin)

# Register your models here.
