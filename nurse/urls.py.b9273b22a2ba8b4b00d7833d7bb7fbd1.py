from django.urls import path

from .views import (
    NurseCreateView,
    NurseDetailView,
    NursePatientListView,

)

urlpatterns = [
    path('<int:pk>/',
         NurseDetailView.as_view(),
         name='nurse_detail'),
    path('new/',
         NurseCreateView.as_view(),
         name='nurse_new'),
    path('patients/',
         LawyerPatientListView.as_view(),
         name='nursepatients_list'),
]
