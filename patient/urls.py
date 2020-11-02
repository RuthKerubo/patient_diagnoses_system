from django.urls import path

from .views import(
    PatientListView,
    PatientCreateView,
    PatientDetailView,
    PatientUpdateView,
)


urlpatterns = [
    path('',
         PatientListView.as_view(),
         name='patient_list'),
    path('new/',
         PatientCreateView.as_view(),
         name='patient_new'),  
    path('<int:pk>/',
         PatientDetailView.as_view(),
         name='patient_detail'),   	
    path('<int:pk>/edit/',
         PatientUpdateView.as_view(),
         name='patient_edit'),
   
    
    


]
