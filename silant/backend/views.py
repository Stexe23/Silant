from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
import users
from .models import *
from .forms import *
from api.serializers import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import generics


# Главная
class HomeView(TemplateView):
    template_name = '/index.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('car_list')
        else:
            return redirect('car_search_list')


class CarSearchView(ListView):
    model = Mashins
    template_name = 'backend/car/car_search.html'
    queryset = Mashins.objects.all()


class CarListView(LoginRequiredMixin, ListView):
    model = Mashins
    template_name = 'backend/car/car_list.html'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = users.objects.get(pk=self.request.user.pk)
            try:
                profile = ClientG.objects.get(name=user)
                if profile.is_service:
                    return Mashins.objects.filter(service_company=profile.service_company)
            except:
                return Mashins.objects.filter(client=user)
        else:
            return Mashins.objects.all()


class CarDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'backend.view_car'
    model = Mashins
    template_name = 'backend/car/car_view.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CarCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'backend.add_car'
    model = Mashins
    form_class = CarForm
    template_name = 'backend/car/car_create.html'
    success_url = reverse_lazy('car_list')


class CarUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'backend.change_car'
    model = Mashins
    form_class = CarForm
    template_name = 'backend/car/car_update.html'
    success_url = reverse_lazy('car_list')


class CarDescriptionView(TemplateView):
    template_name = 'backend/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = Mashins.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'model_mashins':
            context['atribute'] = car.model_mashins
            context['description'] = car.model_mashins.description
        elif atribute == 'model_motor':
            context['atribute'] = car.model_motor
            context['description'] = car.model_motor.description
        elif atribute == 'model_transmission':
            context['atribute'] = car.model_transmission
            context['description'] = car.model_transmission.description
        elif atribute == 'model_drive_bridge':
            context['atribute'] = car.model_drive_bridge
            context['description'] = car.model_drive_bridge.description
        elif atribute == 'model_controll_bridge':
            context['atribute'] = car.model_controll_bridge
            context['description'] = car.model_controll_bridge.description
        elif atribute == 'equipment':
            context['atribute'] = 'Комплектация'
            context['description'] = car.equipment
        elif atribute == 'service_company':
            context['atribute'] = car.service_company
            context['description'] = car.service_company.description
        return context


class CarDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'backend.delete_car'
    model = Mashins
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('car_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'car'
        return context


# API
class CarListAPI(generics.ListAPIView):
    serializer_class = MashinsSerializer
    queryset = Mashins.objects.all()


class CarUserListAPI(generics.ListAPIView):
    serializer_class = MashinsSerializer

    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = Mashins.objects.filter(client=user)
        elif type(user) == str:
            queryset = Mashins.objects.filter(client__username=user)
        return queryset


class CarDetailAPI(generics.RetrieveAPIView):
    serializer_class = MashinsSerializer

    def get_object(self):
        obj = Mashins.objects.get(pk=self.kwargs['pk'])
        return obj


class MaintenanceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'backend.view_maintenance'
    model = TO
    template_name = 'backend/TO/maintenance_list.html'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = users.objects.get(pk=self.request.user.pk)
            try:
                profile = Sersvice.objects.get(name=user)
                if profile.is_service:
                    return TO.objects.filter(service_TO=profile.service_TO)
            except:
                return TO.objects.filter(car__client=user)
        else:
            return TO.objects.all()


class MaintenanceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'backend.add_maintenance'
    model = TO
    form_class = MaintenanceForm
    template_name = 'backend/TO/maintenance_create.html'
    success_url = reverse_lazy('maintenance_list')


class MaintenanceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'backend.change_maintenance'
    model = TO
    form_class = MaintenanceForm
    template_name = 'backend/TO/maintenance_update.html'
    success_url = reverse_lazy('maintenance_list')


class MaintenanceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'backend.delete_maintenance'
    model = TO
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('maintenance_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'maintenance'
        return context


class MaintenanceCarListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'backend.view_maintenance'
    model = TO
    template_name = 'backend/TO/maintenance_car.html'

    def get_queryset(self):
        car = Mashins.objects.get(pk=self.kwargs["pk"])
        return TO.objects.filter(mashins_TO=car)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = Mashins.objects.get(pk=self.kwargs["pk"])
        return context


class ComplaintListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'backend.view_complaint'
    model = Complaint
    template_name = 'backend/complaint/complaint_list.html'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = users.objects.get(pk=self.request.user.pk)
            try:
                profile = ClientG.objects.get(name=user)
                if profile.is_service:
                    return Complaint.objects.filter(service_company=profile.service_company)
            except:
                return Complaint.objects.filter(car__client=user)
        else:
            return Complaint.objects.all()


class ComplaintCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'backend.add_complaint'
    model = Complaint
    form_class = ComplaintForm
    template_name = 'backend/complaint/complaint_create.html'
    success_url = reverse_lazy('complaint_list')


class ComplaintUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'backend.change_complaint'
    model = Complaint
    form_class = ComplaintForm
    template_name = 'backend/complaint/complaint_update.html'
    success_url = reverse_lazy('complaint_list')


class ComplaintDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'backend.delete_complaint'
    model = Complaint
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('complaint_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'сomplaint'
        return context


class ComplaintCarListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'backend.view_complaint'
    model = Complaint
    template_name = 'backend/complaint/complaint_car.html'

    def get_queryset(self):
        car = Mashins.objects.get(pk=self.kwargs["pk"])
        return Complaint.objects.filter(mashins_c=car)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = Mashins.objects.get(pk=self.kwargs["pk"])
        return context


class MaintenanceDescriptionView(TemplateView):
    template_name = 'backend/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        maintenance = TO.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'type':
            context['atribute'] = maintenance.type
            context['description'] = maintenance.type.description
        elif atribute == 'service_company':
            context['atribute'] = maintenance.service_company
            context['description'] = maintenance.service_company.description
        return context


class ComplaintDescriptionView(TemplateView):
    template_name = 'backend/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        complaint = Complaint.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'node_failure':
            context['atribute'] = complaint.node_failure
            context['description'] = complaint.node_failure.description
        elif atribute == 'method_recovery':
            context['atribute'] = complaint.method_recovery
            context['description'] = complaint.method_recovery.description
        elif atribute == 'service_company':
            context['atribute'] = complaint.service_company
            context['description'] = complaint.service_company.description
        return context


# API
class MaintenanceListAPI(generics.ListAPIView):
    serializer_class = TOSerializer
    queryset = TO.objects.all()


class MaintenanceUserListAPI(generics.ListAPIView):
    serializer_class = TOSerializer

    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = TO.objects.filter(car__client=user)
        elif type(user) == str:
            queryset = TO.objects.filter(car__client__username=user)
        return queryset


class MaintenanceDetailAPI(generics.RetrieveAPIView):
    serializer_class = TOSerializer

    def get_object(self):
        obj = TO.objects.get(pk=self.kwargs['pk'])
        return obj


class ComplaintListAPI(generics.ListAPIView):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()


class ComplaintUserListAPI(generics.ListAPIView):
    serializer_class = ComplaintSerializer

    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = Complaint.objects.filter(car__client=user)
        elif type(user) == str:
            queryset = Complaint.objects.filter(car__client__username=user)
        return queryset


class ComplaintDetailAPI(generics.RetrieveAPIView):
    serializer_class = ComplaintSerializer

    def get_object(self):
        obj = Complaint.objects.get(pk=self.kwargs['pk'])
        return obj
