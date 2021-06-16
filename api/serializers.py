# required imports here

from rest_framework.serializers import ModelSerializer

from .models import Patient, HealthOfficer, Hospital, MedicalRecord


# serializers definition here

class HealthOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthOfficer
        fields = ["__all__"]
