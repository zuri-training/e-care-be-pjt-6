from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Patient, HealthOfficer


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
        patient.save()
        return officer
