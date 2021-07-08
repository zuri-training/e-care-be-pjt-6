from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Patient, Hospital, HealthOfficer


class PatientOrHospitalReadOnlyOnPatientRetrieveUpdate(BasePermission):
    message = "You don not have permission to access this view"

    # Patient can edit and view, Hospital can view if Patient is registered with them
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            hospital = Hospital.objects.filter(user=request.user).first()
            patient = Patient.objects.filter(user=request.user).first()

            if hospital:
                return patient in hospital.patients.all()

        return obj.user == request.user


class HospitalOrPatientReadOnlyOnRecordRetrieveUpdate(BasePermission):
    message = "You do not have permission to access this view"

    # Hospital can edit and view, Patient can only view if record is theirs
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return obj.hospital.user == request.user or obj.patient.user == request.user
        
        return obj.hospital.user == request.user


class HospitalOrPatientReadOnlyOnHospitalRetrieveUpdate(BasePermission):
    message = "You do not have permission to access this view"

    # Hospital can edit and view, Patient can only view if record is theirs
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            hospital = Hospital.objects.filter(user=request.user).first()
            patient = Patient.objects.filter(user=request.user).first()

            if patient:
                return True

        return obj.user == request.user


class HealthOfficerOrPatientReadOnlyOnHealthOfficerRetrieveUpdate(BasePermission):
    message = "You do not have permission to access this view"

    # Hospital can edit and view, Patient can only view if record is theirs
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            health_officer = HealthOfficer.objects.filter(user=request.user).first()
            patient = Patient.objects.filter(user=request.user).first()

            if patient:
                return True

        return obj.user == request.user
