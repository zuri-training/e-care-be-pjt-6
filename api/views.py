from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Patient, HealthOfficer, MedicalRecord, Hospital
from .serializers import (
    PatientSerializer,
    HealthOfficerSerializer,
    MedicalRecordSerializer,
    HospitalSerializer
)


class APIDocumentationView(APIView):
    
    def get(self, request, format=None):
        postman_doc_link = "https://documenter.getpostman.com/view/16360417/TzecBjvf"
        return redirect(postman_doc_link, permanent=True)


# Create your views here.
class PatientCreateAPIView(APIView):
    serializer_class = PatientSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientListAPIView(APIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        patients = Patient.objects.all()
        serializer = self.serializer_class(patients, many=True)
        return Response(serializer.data)


class PatientRetrieveUpdateAPIView(APIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, uuid, format=None):
        patient = Patient.objects.filter(uuid=uuid).first()

        if patient:
            serializer = self.serializer_class(patient)
            return Response(serializer.data)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, uuid, format=None):
        patient = Patient.objects.filter(uuid=uuid).first()

        if patient:
            serializer = self.serializer_class(
                instance=patient, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(updated=timezone.now())
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_404_NOT_FOUND)


class HealthOfficerCreateAPIView(APIView):
    serializer_class = HealthOfficerSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HealthOfficerListAPIView(APIView):
    serializer_class = HealthOfficerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        officers = HealthOfficer.objects.all()
        serializer = self.serializer_class(officers, many=True)
        return Response(serializer.data)


class HealthOfficerRetrieveUpdateAPIView(APIView):
    serializer_class = HealthOfficerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, uuid, format=None):
        officer = HealthOfficer.objects.filter(uuid=uuid).first()

        if officer:
            serializer = self.serializer_class(officer)
            return Response(serializer.data)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, uuid, format=None):
        officer = HealthOfficer.objects.filter(uuid=uuid).first()

        if officer:
            serializer = self.serializer_class(
                instance=officer, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(updated=timezone.now())
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_404_NOT_FOUND)


class MedicalRecordCreateAPIView(APIView):
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, format=None):
        hospital = Hospital.objects.filter(user=request.user).first()
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(hospital=hospital)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class MedicalRecordListAPIView(APIView):
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        hospital = Hospital.objects.filter(user=request.user).first()

        if hospital:
            medical_records = MedicalRecord.objects.filter(hospital=hospital).all()
            serializer = self.serializer_class(medical_records, many=True)
            return Response(serializer.data)
        return Response({}, status=status.HTTP_404_NOT_FOUND)


class MedicalRecordRetrieveUpdateAPIView(APIView):
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, uuid, format=None):
        medical_record = Hospital.objects.filter(user=request.user).first()\
            .medicalrecord_set.filter(uuid=uuid).first()

        if medical_record:
            serializer = self.serializer_class(medical_record)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
            
    
    def put(self, request, uuid, format=None):
        medical_record = Hospital.objects.filter(user=request.user).first()\
            .medicalrecord_set.filter(uuid=uuid).first()

        if medical_record:
            serializer = self.serializer_class(
                instance=medical_record, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(updated=timezone.now())
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_404_NOT_FOUND)


class HospitalCreateAPIView(APIView):
    serializer_class = HospitalSerializer
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HospitalListAPIView(APIView):
    serializer_class = HospitalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        hospitals = Hospital.objects.all()
        serializer = self.serializer_class(hospitals, many=True)
        return Response(serializer.data)


class HospitalRetrieveUpdateAPIView(APIView):
    serializer_class = HospitalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, uuid, format=None):
        hospital = Hospital.objects.filter(uuid=uuid).first()

        if hospital:
            serializer = self.serializer_class(hospital)
            return Response(serializer.data)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, uuid, format=None):
        hospital = Hospital.objects.filter(uuid=uuid).first()

        if hospital:
            serializer = self.serializer_class(instance=hospital, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
