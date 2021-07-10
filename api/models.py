import uuid

from django.db import models

from rest_framework.reverse import reverse_lazy


# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    other_name = models.CharField(max_length=32, null=True, blank=True)
    phone_number = models.CharField(max_length=16, unique=True)
    gender = models.CharField(max_length=8, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=32, null=True, blank=True)
    lga = models.CharField(max_length=64, null=True, blank=True)
    state = models.CharField(max_length=32, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    def __repr__(self):
        return str(self.user)
    
    __str__ = __repr__

    def get_absolute_url(self):
        return reverse_lazy('patient-get-update', args=[str(self.uuid)])


class HealthOfficer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    other_name = models.CharField(max_length=32, null=True, blank=True)
    phone_number = models.CharField(max_length=16, unique=True)
    gender = models.CharField(max_length=8, null=True, blank=True)
    specialty = models.CharField(max_length=64, null=True, blank=True)
    role = models.CharField(max_length=64, null=True, blank=True)
    licence = models.CharField(max_length=256, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    last_seen = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    def __repr__(self):
        return str(self.user)
    
    __str__ = __repr__

    def get_absolute_url(self):
        return reverse_lazy('health-officer-get-update', args=[str(self.uuid)])


class Hospital(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=256)
    specialty = models.CharField(max_length=64, default='general')
    city = models.CharField(max_length=16)
    lga = models.CharField(max_length=64)
    state = models.CharField(max_length=16)
    address = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    patients = models.ManyToManyField('Patient', related_name="hospitals")
    health_officers = models.ManyToManyField('HealthOfficer', related_name="hospitals")

    def __repr__(self):
        return str(self.name)
    
    __str__ = __repr__

    def get_absolute_url(self):
        return reverse_lazy('hospital-get-update', args=[str(self.uuid)])


class MedicalRecord(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    test_category = models.CharField(max_length=256, default='Examine')
    test_type = models.CharField(max_length=256, default='Blood Test')
    test_result = models.TextField(default='')
    prescription = models.TextField(default='')
    hospital = models.ForeignKey(
        'Hospital', related_name="records", on_delete=models.CASCADE)
    patient = models.ForeignKey(
        'Patient', related_name="records", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    def __repr__(self):
        return str(self.test_category)
    
    __str__ = __repr__

    def get_absolute_url(self):
        return reverse_lazy('medical-record-get-update', args=[str(self.uuid)])
