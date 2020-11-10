from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from bootstrap_datepicker_plus import DatePickerInput
from django.urls import reverse_lazy

from .models import Diagnosis
from patient.models import Patient

from django import forms

from rest_framework import viewsets

from .serializers import DiagnosisSerializer


class DiagnosisListView(LoginRequiredMixin, ListView):
    model = Diagnosis
    ordering = ['patient', 'medical_diagnosis']
    template_name = 'diagnoses/list.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden to ensure that the passed primary key does exist
        """
        self.patient = get_object_or_404(Patient, pk=kwargs['patient_pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """
        Return only the diagnoses for the passed patient
        """
        return Diagnosis.objects.filter(
            patient=self.patient).order_by('medical_diagnosis')


class DiagnosisDetailView(LoginRequiredMixin, DetailView):
    model = Diagnosis
    template_name = 'diagnoses/detail.html'
    login_url = 'login'


class DiagnosisUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Diagnosis
    fields = ('medical_diagnosis', 'description',
              'nursing_diagnosis', 'by_specialist_nurse', 'date')
    template_name = 'diagnoses/edit.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser


class DiagnosisCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Diagnosis
    fields = ('patient', 'medical_diagnosis', 'description',
              'date', 'by_specialist_nurse')
    template_name = 'diagnoses/new.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden to ensure that the passed primary key does exist
        """
        self.patient = get_object_or_404(Patient, pk=kwargs['patient_pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view
        """
        initial = super(DiagnosisCreateView, self).get_initial()
        initial['patient'] = self.patient
        return initial

    def get_form(self):
        """
        Overridden to change the DateFields from text boxes to
        DatePicker widgets
        """
        form = super(DiagnosisCreateView, self).get_form()

        return form


class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all().order_by('patient')
    serializer_class = DiagnosisSerializer
# Create your views here.
