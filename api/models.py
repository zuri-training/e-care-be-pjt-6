import uuid

from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    phone_number = models.CharField(max_length=16, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    other_name = models.CharField(max_length=64, null=True, blank=True)
    gender = models.CharField(max_length=16, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    profession = models.CharField(max_length=64, null=True, blank=True)
    marital_status = models.CharField(max_length=16, null=True, blank=True)
    city = models.CharField(max_length=16, null=True, blank=True)
    lga = models.CharField(max_length=32, null=True, blank=True)
    state = models.CharField(max_length=16, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    last_seen = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    hospitals = models.ManyToManyField('Hospital')

    def __repr__(self):
        return self.user.__repr__()
    
    def __str__(self):
        return self.user.__str__()


class Hospital(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=256, unique=True)
    city = models.CharField(max_length=16)
    lga = models.CharField(max_length=32)
    state = models.CharField(max_length=16)
    address = models.TextField()
    specialty = models.CharField(max_length=64)

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name


class MedicalRecord(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    category = models.CharField(max_length=64, default='Examine')
    test_type = models.CharField(max_length=128)
    result = models.TextField()
    prescription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False)
    health_officer = models.ForeignKey('HealthOfficer', on_delete=models.CASCADE)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)

    def __repr__(self):
        return "<Medical Record {}>".format(self.id)
    
    def __str__(self):
        return self.__repr__()


class HealthOfficer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    phone_number = models.CharField(max_length=16, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    other_name = models.CharField(max_length=64, null=True, blank=True)
    gender = models.CharField(max_length=16, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    specialty = models.CharField(max_length=64, null=True, blank=True)
    marital_status = models.CharField(max_length=16, null=True, blank=True)
    city = models.CharField(max_length=16, null=True, blank=True)
    lga = models.CharField(max_length=32, null=True, blank=True)
    state = models.CharField(max_length=16, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    last_seen = models.DateTimeField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    hospitals = models.ManyToManyField('Hospital')

    def __repr__(self):
        return self.user.__repr__()
    
    def __str__(self):
        return self.user.__str__()
