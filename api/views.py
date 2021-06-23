from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import Redirect

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
        return Redirect(postman_doc_link, permanent=True)


# Create your views here.
class PatientCreateListAPIView(APIView):
    serializer_class = PatientSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        patients = Patient.objects.all()
        serializer = self.serializer_class(patients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_404_NOT_FOUND)


class HealthOfficerCreateListAPIView(APIView):
    serializer_class = HealthOfficerSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        officers = HealthOfficer.objects.all()
        serializer = self.serializer_class(officers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_404_NOT_FOUND)


class MedicalRecordListCreateAPIView(APIView):
    serializer_class = MedicalRecordSerializer

    def get(self, request, uuid, format=None):
        patient = Patient.objects.filter(uuid=uuid).first()

        if patient:
            medical_records = MedicalRecord.objects.filter(patient=patient).all()
            serializer = self.serializer_class(medical_records, many=True)
            return Response(serializer.data)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, uuid, format=None):
        patient = Patient.objects.filter(uuid=uuid).first()

        if patient:
            context = {'patient': patient}
            serializer = self.serializer_class(data=request.data, context=context)
        
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_404_NOT_FOUND)


class MedicalRecordRetrieveUpdateAPIView(APIView):
    serializer_class = MedicalRecordSerializer

    # uuid1-Patient uuid, uuid2-MedicalRecord uuid
    def get(self, request, uuid1, uuid2, format=None):
        try:
            patient = Patient.objects.filter(uuid=uuid1).first()
            medical_record = patient.medicalrecord_set.filter(uuid=uuid2).first()
        except ObjectDoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(medical_record)
        return Response(serializer.data)
    
    def put(self, request, uuid1, uuid2, format=None):
        try:
            patient = Patient.objects.filter(uuid=uuid1).first()
            medical_record = patient.medicalrecord_set.filter(uuid=uuid2).first()
        except ObjectDoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(
            instance=medical_record, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HospitalCreateListAPIView(APIView):
    serializer_class = HospitalSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        hospitals = Hospital.objects.all()
        serializer = self.serializer_class(hospitals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        return Response({}, status=status.HTTP_404_NOT_FOUND)
