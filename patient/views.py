from django.shortcuts import render

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy

from .models import Patient


class PatientListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Patient
    ordering = ['id_number', 'first_name', 'surname']
    template_name = 'patient/list.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'patient/detail.html'
    login_url = 'login'


class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Patient
    fields = ('id_number', 'first_name', 'surname')
    template_name = 'patient/edit.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser


class PatientCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Patient
    fields = ('id_number', 'first_name', 'surname')
    template_name = 'patient/new.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser
        return super().form_valid(form)

# Create your views here.
