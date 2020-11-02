from django.shortcuts import render

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Specialist, SpecialistPatient


class SpecialistDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Specialist
    template_name = 'specialist/detail.html'
    login_url = 'login'

    def test_func(self):
        is_specialist = Specialist.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_specialist


class SpecialistCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Specialist
    fields = ('user',)
    template_name = 'specialist/new.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser
        
        
class SpecialistPatientCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = SpecialistPatient
    fields = ('patient',)
    template_name = 'specialistpatient/new.html'
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
        specialist = get_object_or_404(Specialist, user=user)
        form.instance.specialist = specialist
        return super(SpecialistPatientCreateView, self).form_valid(form)

    def test_func(self):
        is_specialist = Specialist.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_specialist
        
        
class SpecialistPatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SpecialistPatient
    fields = ('patient',)
    template_name = 'specialistpatient/edit.html'
    login_url = 'login'

    def test_func(self):
        is_specialist = Specialist.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_specialist


class SpecialistPatientListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = SpecialistPatient
    template_name = 'specialistpatient/list.html'
    login_url = 'login'

    def test_func(self):
        is_specialist = Specialist.objects.filter(user=self.request.user).exists()
        return self.request.user.is_superuser or is_specialist

    def get_queryset(self):
        """
        Return only the patients for the current nurse
        """
        specialist = Specialist.objects.filter(user=self.request.user).first()
        return SpecialistPatient.objects.filter(
            specialist=specialist)


# Create your views here.
