from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    PatientCreateAPIView,
    PatientListAPIView,
    PatientRetrieveUpdateAPIView,
    HealthOfficerRetrieveUpdateAPIView,
    HealthOfficerCreateAPIView,
    HealthOfficerListAPIView,
    MedicalRecordCreateAPIView,
    MedicalRecordListAPIView,
    MedicalRecordRetrieveUpdateAPIView,
    HospitalCreateAPIView,
    HospitalListAPIView,
    HospitalRetrieveUpdateAPIView,
    APIDocumentationView
)


urlpatterns = [
    path('docs/', APIDocumentationView.as_view(), name='api-docs'),
    
    path(
         'user/patient/register/',
         PatientCreateAPIView.as_view(),
         name='patient-create'
    ),
    
    path(
        'user/patients/',
        PatientListAPIView.as_view(),
        name='patient-list'
    ),
    
    path(
         'user/patient/<str:uuid>/',
         PatientRetrieveUpdateAPIView.as_view(),
         name='patient-get-update'
    ),


    path(
         "user/health-officer/register/",
         HealthOfficerCreateAPIView.as_view(),
         name="health-officer-create"
    ),
    
    path(
        'user/health-officers/',
        HealthOfficerListAPIView.as_view(),
        name='health-officer-list'
    ),
    
    path(
         "user/health-officer/<str:uuid>/",
         HealthOfficerRetrieveUpdateAPIView.as_view(),
         name="health-officer-get-update"
    ),

    path(
        'user/patient/<str:uuid>/record/new/',
         MedicalRecordCreateAPIView.as_view(),
         name='medical-record-create'
    ),
    
    path(
        'user/patient/<str:uuid>/records/',
         MedicalRecordListAPIView.as_view(),
         name='medical-record-list'
    ),

    path(
        'user/patient/<str:uuid1>/record/<str:uuid2>/',
        MedicalRecordRetrieveUpdateAPIView.as_view(),
        name='medical-record-get-update'
    ),

    path(
        'hospital/register/',
        HospitalCreateAPIView.as_view(),
        name='hospital-create'
    ),
    
    path(
        'hospitals/',
        HospitalListAPIView.as_view(),
        name='hospital-list'
    ),

    path(
        'hospital/<str:uuid>/',
        HospitalRetrieveUpdateAPIView.as_view(),
        name='hospital-update'
    ),

    path(
        'user/login/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    
    path(
        'user/login/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),


]
