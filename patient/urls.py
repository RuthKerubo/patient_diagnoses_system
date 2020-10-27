from django.urls import path

from .views import(
    PatientListView,
    PatientCreateView,
    PatientDetailView,
    PatientUpdateView,
)


urlpatterns = [
    path('<int:pk>/edit/',
         PatientUpdateView.as_view(),
         name='patient_edit'),
    path('<int:pk>/',
         PatientDetailView.as_view(),
         name='patient_detail'),
    path('new/',
         PatientCreateView.as_view(),
         name='patient_new'),
    path('',
         PatientListView.as_view(),
         name='patient_list'),


]
