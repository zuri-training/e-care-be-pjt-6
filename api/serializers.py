# required imports here

from rest_framework.serializers import ModelSerializer

from .models import Patient, HealthOfficer, Hospital, MedicalRecord


# serializers definition here

class HealthOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthOfficer
        fields = ["user",
                  "phone_number",
                  "first_name",
                  "last_name",
                  "other_name ",
                  "gender",
                  "date_of_birth",
                  "age",
                  "specialty",
                  "marital_status",
                  "city",
                  "lga",
                  "state",
                  "address",
                  "last_seen",
                  "created_at",
                  "updated_at",
                  "hospitals",
                  ]
