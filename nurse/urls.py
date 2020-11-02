from django.urls import path

from .views import (
    NurseCreateView,
    NurseDetailView,
    NursePatientCreateView,
    NursePatientUpdateView,
    NursePatientListView,

)

urlpatterns = [
    path('<int:pk>/',
         NurseDetailView.as_view(),
         name='nurse_detail'),
    path('new/',
         NurseCreateView.as_view(),
         name='nurse_new'),
    path('patient/new/',
         NursePatientCreateView.as_view(),
         name='nursepatient_new'),
    path('patient/<int:pk>/edit/',
         NursePatientUpdateView.as_view(),
         name='nursepatient_edit'),
    path('patients/',
         NursePatientListView.as_view(),
         name='nursepatients_list'),
]
