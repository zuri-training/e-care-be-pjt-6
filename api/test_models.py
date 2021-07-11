from django.test import TestCase
from .models import Patient, HealthOfficer, Hospital
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model




class PatientModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            first_name='lanre',
            last_name = 'titi',
            other_name = 'dede',
            phone_number = '08123456789',
            gender = 'male',
            date_of_birth='27Nov1996',
            city='ketu',
            lga='kosofe',
            state='lagos',
            address='12 sdjfjf hdhfh',
        )

    def test_patient_list_view(self):
        response = self.client.get('user/patients/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '')

    def test_patient_create_view(self):
        response = self.client.get('user/patient/register/')
        self.assertEqual(f'{self.patient.first_name}', 'lanre')
        self.assertEqual(f'{self.patient.last_name}', 'titi')
        self.assertEqual(f'{self.patient.other_name}', 'dede')
        self.assertEqual(f'{self.patient.phone_number}', '08123456789')
        self.assertEqual(f'{self.patient.gender}', 'male')
        self.assertEqual(f'{self.patient.date_of_birth}', '27Nov1996')
        self.assertEqual(f'{self.patient.city}', 'ketu')
        self.assertEqual(f'{self.patient.lga}', 'kosofe')
        self.assertEqual(f'{self.patient.state}', 'lagos')
        self.assertEqual(f'{self.patient.address}', '12 sdjfjf hdhfh')

    def test_get_absolute_url(self):
        patient = Patient.objects.get(id=1)
        self.assertEqual(patient.get_absolute_url(), 'user/patient/<str:uuid>/')


class HealthOfficerModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            first_name='lanre',
            last_name='titi',
            other_name='dede',
            phone_number='08123456789',
            gender='male',
            specialty= '',
            date_of_birth='27Nov1996',
            city='ketu',
            lga='kosofe',
            state='lagos',
            role= '',
            license= ''
        )

    def test_health_officer_list_view(self):
        response = self.client.get('user/health-officers/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '')

    def test_health_officer_create_view(self):
        response = self.client.get('user/patient/register/')
        self.assertEqual(f'{self.healthofficer.first_name}', 'lanre')
        self.assertEqual(f'{self.healthofficer.last_name}', 'titi')
        self.assertEqual(f'{self.healthofficer.other_name}', 'dede')
        self.assertEqual(f'{self.healthofficer.phone_number}', '08123456789')
        self.assertEqual(f'{self.healthofficer.gender}', 'male')
        self.assertEqual(f'{self.healthofficer.specialty}', '')
        self.assertEqual(f'{self.healthofficer.date_of_birth}', '27Nov1996')
        self.assertEqual(f'{self.healthofficer.city}', 'ketu')
        self.assertEqual(f'{self.healthofficer.lga}', 'kosofe')
        self.assertEqual(f'{self.healthofficer.state}', 'lagos')
        self.assertEqual(f'{self.healthofficer.role}', '')
        self.assertEqual(f'{self.healthofficer.license}', '')


    def test_get_absolute_url(self):
        healthofficer = HealthOfficer.objects.get(id=1)
        self.assertEqual(healthofficer.get_absolute_url(), "user/health-officer/<str:uuid>/")


class HospitalModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            name='lanreHospitals',
            specialty='',
            city='ketu',
            lga='kosofe',
            state='lagos',
            address='12 sdjfjf hdhfh',

        )

    def test_hospital_list_view(self):
        response = self.client.get('user/hospitals/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '')

    def test_hospital_create_view(self):
        response = self.client.get('user/patient/register/')
        self.assertEqual(f'{self.hospital.name}', 'lanreHospitals')
        self.assertEqual(f'{self.hospital.specialty}', '')
        self.assertEqual(f'{self.hospital.city}', 'ketu')
        self.assertEqual(f'{self.hospital.lga}', 'kosofe')
        self.assertEqual(f'{self.hospital.state}', 'lagos')
        self.assertEqual(f'{self.hospital.address}', '12 sdjfjf hdhfh')


    def test_get_absolute_url(self):
        hospital = Hospital.objects.get(id=1)
        self.assertEqual(hospital.get_absolute_url(), 'user/hospital/<str:uuid>/')







