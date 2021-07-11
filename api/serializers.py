from django.contrib.auth.models import User

from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Patient, HealthOfficer, MedicalRecord, Hospital


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD


class CustomTokenObtainPairSerializer(EmailTokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add type of user to the payload
        user_categories = ["patient", "health_officer", "hospital"]
        request_user_category = None
        for user_category in user_categories:
            if getattr(user, user_category, None) is not None:
                request_user_category = user_category
                break

        token['usertype'] = request_user_category

        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["access"] = str(refresh.access_token)
        data["usertype"] = str(refresh.payload["usertype"])
        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class MedicalRecordSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = MedicalRecord
        fields = '__all__'
        read_only_fields = ['id', 'created', 'updated', 'hospital']


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    url = serializers.URLField(source='get_absolute_url', read_only=True)
    records = MedicalRecordSerializer(many=True, read_only=True)
    hospitals = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Patient
        fields = "__all__"
        read_only_fields = ['id', 'created', 'updated']


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        patient = Patient.objects.create(**validated_data, user=user)
        patient.save()
        return patient


class HealthOfficerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    url = serializers.URLField(source='get_absolute_url', read_only=True)
    hospitals = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = HealthOfficer
        fields = '__all__'
        read_only_fields = [
            'id', 'is_verified', 'is_admin',
            'last_seen', 'created', 'updated'
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        officer = HealthOfficer.objects.create(**validated_data, user=user)
        officer.save()
        return officer


class HospitalSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Hospital
        fields = '__all__'
        read_only_fields = ['id', 'patients', 'health_officers', 'created']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        hospital = Hospital.objects.create(**validated_data, user=user)
        hospital.save()
        return hospital
