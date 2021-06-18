from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Patient
from .serializers import PatientSerializer


# Create your views here.
class PatientCreateListAPIView(APIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

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
            serializer = self.serializer_class(instance=patient, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
