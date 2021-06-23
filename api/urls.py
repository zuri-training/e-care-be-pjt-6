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
    MedicalRecordListCreateAPIView,
    MedicalRecordRetrieveUpdateAPIView,
    HospitalCreateAPIView,
    HospitalListAPIView,
    HospitalRetrieveUpdateAPIView
)


urlpatterns = [
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
        'user/patient/<str:uuid>/records/',
         MedicalRecordListCreateAPIView.as_view(),
         name='medical-record-get-create'
    ),

    path(
        'user/patient/<str:uuid1>/records/<str:uuid2>/',
        MedicalRecordRetrieveUpdateAPIView.as_view(),
        name='medical-record-get-update'
    ),

    path(
        'user/hospital/register/',
        HospitalCreateAPIView.as_view(),
        name='hospital-create'
    ),
    
    path(
        'user/hospitals/',
        HospitalListAPIView.as_view(),
        name='hospital-list'
    ),

    path(
        'user/hospital/<str:uuid>/',
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
