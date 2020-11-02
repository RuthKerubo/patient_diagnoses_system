from django.shortcuts import render

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Nurse, NursePatient


class NurseDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Nurse
    template_name = 'nurse/detail.html'
    login_url = 'login'

    def test_func(self):
        is_nurse = Nurse.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_nurse


class NurseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Nurse
    fields = ('user',)
    template_name = 'nurse/new.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser
        
        
class NursePatientCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = NursePatient
    fields = ('patient',)
    template_name = 'nursepatient/new.html'
    login_url = 'login'

    # def get_initial(self):
        # initial = super(LawyerClientCreateView, self).get_initial()
        # user = self.request.user
        # lawyer = get_object_or_404(Lawyer, user=user)
        # initial['lawyer'] = lawyer
        # return initial

    def form_valid(self, form):
        """
        Overridden to always set the lawyer to the currently
        logged in user
        """
        user = self.request.user
        nurse = get_object_or_404(Nurse, user=user)
        form.instance.nurse = nurse
        return super(NursePatientCreateView, self).form_valid(form)

    def test_func(self):
        is_nurse = Nurse.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_nurse
        
        
class NursePatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NursePatient
    fields = ('patient',)
    template_name = 'nursepatient/edit.html'
    login_url = 'login'

    def test_func(self):
        is_nurse = Nurse.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_nurse


class NursePatientListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = NursePatient
    template_name = 'nursepatient/list.html'
    login_url = 'login'

    def test_func(self):
        is_nurse = Nurse.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_nurse

    def get_queryset(self):
        """
        Return only the patients for the current nurse
        """
        nurse = Nurse.objects.filter(user=self.request.user).first()
        return NursePatient.objects.filter(
            nurse=nurse)


# Create your views here.
