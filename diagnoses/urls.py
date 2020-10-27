from django.urls import path

from .views import (
    DiagnosisListView,
    DiagnosisCreateView,
    DiagnosisDetailView,
    DiagnosisUpdateView,
)

urlpatterns = [
    path('<int:pk>/edit/',
         DiagnosisUpdateView.as_view(),
         name='diagnoses_edit'),
    path('<int:pk>/',
         DiagnosisDetailView.as_view(),
         name='diagnoses_detail'),
    path('new/<int:patient_pk>/',
         DiagnosisCreateView.as_view(),
         name='diagnoses_new'),
    path('list/<int:patient_pk>',
         DiagnosisListView.as_view(),
         name='diagnoses_list'),
]
