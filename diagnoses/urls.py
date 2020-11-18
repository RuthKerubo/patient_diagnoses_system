from django.urls import include, path

from rest_framework import routers

from . import views

from .views import (
    DiagnosisListView,
    DiagnosisUpdateView,
    DiagnosisDetailView,
    DiagnosisCreateView
)

router = routers.DefaultRouter()
router.register(r'diagnoses', views.DiagnosisViewSet)


urlpatterns = [

    path('list/<int:patient_pk>/',
         DiagnosisListView.as_view(), name='diagnosis_list'),
    path('<int:pk>/edit/',
         DiagnosisUpdateView.as_view(), name='diagnosis_edit'),
    path('<int:pk>/',
         DiagnosisDetailView.as_view(), name='diagnosis_detail'),
    path('new/<int:patient_pk>/',
         DiagnosisCreateView.as_view(), name='diagnosis_new'),
    
    path('dashboard/', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    
    path('data', views.pivot_data, name='pivot_data'),        
    
    path('', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),                  
]
