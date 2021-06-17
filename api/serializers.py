# required imports here

from rest_framework.serializers import ModelSerializer

from .models import Patient, HealthOfficer, Hospital, MedicalRecord


# serializers definition here

class HealthOfficerSerializer(ModelSerializer):
    class Meta:
        model = HealthOfficer
        fields = "__all__"

class HospitalSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"