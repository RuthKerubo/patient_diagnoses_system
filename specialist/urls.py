from django.urls import path

from .views import (
    SpecialistCreateView,
    SpecialistDetailView,
    SpecialistPatientCreateView,
    SpecialistPatientUpdateView,
    SpecialistPatientListView,

)

urlpatterns = [
    path('<int:pk>/',
         SpecialistDetailView.as_view(),
         name='specialist_detail'),
    path('new/',
         SpecialistCreateView.as_view(),
         name='specialist_new'),
    path('patient/new/',
         SpecialistPatientCreateView.as_view(),
         name='specialistpatient_new'),
    path('patient/<int:pk>/edit/',
         SpecialistPatientUpdateView.as_view(),
         name='specialistpatient_edit'),
    path('patients/',
         SpecialistPatientListView.as_view(),
         name='specialistpatients_list'),
]
