from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import PatientCreateListAPIView, PatientRetrieveUpdateAPIView, HealthOfficerRetrieveUpdateAPIView, HealthOfficerCreateListAPIView


urlpatterns = [
    path('user/patients/', PatientCreateListAPIView.as_view(),
         name='patient-list-create'),
    path('user/patients/<str:uuid>/',
         PatientRetrieveUpdateAPIView.as_view(), name='patient-get-update'),


    path("user/health-officer/", HealthOfficerCreateListAPIView.as_view(),
         name="health-officer-list-create"),
    path("user/health-officer/<str:uuid>/",
         HealthOfficerRetrieveUpdateAPIView.as_view(), name="health-officer-get-update"),

    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
