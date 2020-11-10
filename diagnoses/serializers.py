from rest_framework import serializers

from .models import Diagnosis


class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ('patient', 'medical_diagnosis', 'description',
                  'nursing_diagnosis', 'by_specialist_nurse', 'date')
