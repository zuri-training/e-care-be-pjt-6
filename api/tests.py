from django.utils import timezone

from django.test import TestCase
from django.contrib.auth.models import User

from .models import Patient, HealthOfficer, Hospital, MedicalRecord


class ModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='username1', password='password1', email='email1@gmail.com'
        )
        self.user1.save()
        self.user2 = User.objects.create_user(
            username='username2', password='password2', email='email2@gmail.com'
        )
        self.user2.save()
        self.patient1 = Patient.objects.create(
            user=self.user1, first_name='first1', last_name='last1', other_name='other1',
            gender='male', date_of_birth=timezone.datetime(day=8,month=9,year=1998), age=23,
            profession='Lawyer', marital_status='single', city='MyCity', lga='MyLGA',
            state='MyState', address='my address'
        )
        self.patient1.save()

        self.patient2 = Patient.objects.create(
            user=self.user2, first_name='first2', last_name='last2', other_name='other2',
            gender='male', date_of_birth=timezone.datetime(day=8,month=9,year=1998), age=23,
            profession='Doctor', marital_status='single', city='MyCity', lga='MyLGA',
            state='MyState', address='my address'
        )
        self.patient2.save()
        
        self.officer1 = HealthOfficer.objects.create(
            user=self.user2, first_name='first2', last_name='last2', other_name='other2',
            gender='male', date_of_birth=timezone.datetime(day=8,month=9,year=1990), age=31,
            specialty='surgery', marital_status='married', city='MyCity2', lga='MyLGA2',
            state='MyState2', address='my address2'
        )
        self.officer1.save()

        self.hospital1 = Hospital.objects.create(
            name='General Hospital MyCity', city='MyCity', lga='MyLGA', state='MyState',
            address='number 22 website street development', specialty='Surgery'
        )
        self.hospital1.save()

        self.hospital2 = Hospital.objects.create(
            name='General Hospital MyCity 2', city='MyCity 2', lga='MyLGA 2', state='MyState 2',
            address='number 55 website street development', specialty='Optometry'
        )
        self.hospital2.save()

        self.medical_record1 = MedicalRecord.objects.create(
            category='Analysis', test_type='CT Scan of Abdomen',
            result='Little abnormal growth on the large intestine',
            prescription='daily intake of 5 litres of water, Eating dinner latest 5PM',
            patient=self.patient1, health_officer=self.officer1, hospital=self.hospital1
        )
        self.medical_record1.save()

        self.medical_record2 = MedicalRecord.objects.create(
            category='Examine', test_type='Blood Test',
            result='Negative',
            prescription='',
            patient=self.patient1, health_officer=self.officer1, hospital=self.hospital1
        )
        self.medical_record2.save()
    
    def test_all_models_can_instantiate_and_save(self):
        self.assertTrue(self.user1 != None)
        self.assertTrue(self.patient1 != None)
        self.assertTrue(self.officer1 != None)
        self.assertTrue(self.hospital1 != None)
        self.assertTrue(self.medical_record1 != None)
    
    def test_many_to_many_relationship_with_patient_and_hospital(self):
        self.patient1.hospitals.add(self.hospital1)
        self.patient1.hospitals.add(self.hospital2)
        self.patient1.save()
        self.patient2.hospitals.add(self.hospital1)
        self.patient2.hospitals.add(self.hospital2)
        self.assertTrue(len(self.patient1.hospitals.all()) == 2)
        self.assertTrue(len(self.patient2.hospitals.all()) == 2)
        self.assertTrue(len(self.hospital1.patient_set.all()) == 2)
        self.assertTrue(len(self.hospital2.patient_set.all()) == 2)
    
    def test_one_to_many_relationship_with_patient_and_medical_record(self):
        patient = self.medical_record1.patient
        self.assertEqual(patient, self.patient1)
        self.assertEqual(len(self.patient1.medicalrecord_set.all()), 2)

    def test_one_to_many_relationship_with_health_officer_and_medical_record(self):
        officer = self.medical_record1.health_officer
        self.assertEqual(officer, self.officer1)
        self.assertEqual(len(self.officer1.medicalrecord_set.all()), 2)
    
    def test_many_to_many_relationship_with_health_officer_and_hospital(self):
        self.officer1.hospitals.add(self.hospital1)
        self.officer1.hospitals.add(self.hospital2)
        self.assertEqual(len(self.officer1.hospitals.all()), 2)
        self.assertEqual(len(self.hospital1.healthofficer_set.all()), 1)
