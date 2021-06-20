from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Patient, HealthOfficer, MedicalRecord


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        patient = Patient.objects.create(**validated_data, user=user)
        patient.save()
        return patient


class HealthOfficerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = HealthOfficer
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        officer = HealthOfficer.objects.create(**validated_data, user=user)
        officer.save()
        return officer


class MedicalRecordSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = MedicalRecord
        fields = '__all__'
    
    def create(self, validated_data):
        medical_record = MedicalRecord.objects.create(
            **validated_data, patient=self.context['patient'])
        medical_record.save()
        return medical_record
