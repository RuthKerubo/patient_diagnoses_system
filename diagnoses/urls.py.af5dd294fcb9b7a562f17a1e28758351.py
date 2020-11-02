from django.urls import path

from .views import (
    DiagnosisListView,
    DiagnosisUpdateView,
    DiagnosisDetailView,
    DiagnosisCreateView
)


urlpatterns = [
    path('list/<int:patient_pk>/',
         DiagnosisListView.as_view(), name='diagnosis_list'),
    path('<int:pk>/edit/',
         DiagnosisUpdateView.as_view(), name='diagnosis_edit'),
    path('<int:pk>/',
         DiagnosisDetailView.as_view(), name='diagnosis_detail'),
    path('new/<int:patient_pk>/',
         DiagnosisCreateView.as_view(), name='diagnosis_new'),
]
