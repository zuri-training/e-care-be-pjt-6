import uuid

from django.db import models
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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    def __repr__(self):
        return str(self.user)
    
    __str__ = __repr__

    def get_absolute_url(self):
        return reverse_lazy('get-update', args=[str(self.uuid)])

