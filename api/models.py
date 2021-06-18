import uuid

from django.db import models
from django.db.models.query import FlatValuesListIterable
from django.urls import reverse_lazy

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    other_name = models.CharField(max_length=32, null=True, blank=True)
    phone_number = models.CharField(max_length=16, unique=True)
    gender = models.CharField(max_length=8, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    city = models.CharField(max_length=32, null=True, blank=True)
    lga = models.CharField(max_length=64, null=True, blank=True)
    state = models.CharField(max_length=32, null=True, blank=True)
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

