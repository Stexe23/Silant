from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

import users
from .models import *
from .forms import *
from api.serializers import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import generics, request


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
    model = Mashins,
    template_name = 'backend/car/car_list.html'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = CustomUser.objects.get(pk=self.request.user.pk)
            try:
                clients = ClientG.objects.get(name_id=user)
                car = Mashins.objects.filter(client=clients)
                return car
            except:
                servic = Sersvice.objects.get(name_id=user)
                car = Mashins.objects.filter(service_company=servic)
                return car
        else:
            return Mashins.objects.all()


class MaintenanceListView(LoginRequiredMixin, ListView):
    model = TO
    ordering = 'mashins_TO'
    template_name = 'backend/TO/maintenance_list.html'
    context_object_name = 'mashins_TO'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = CustomUser.objects.get(pk=self.request.user.pk)

            try:
                clients = ClientG.objects.filter(name_id=user.pk)
                mashins = Mashins.objects.filter(client=clients)
                for m in mashins:
                    yield TO.objects.filter(mashins_TO=m)
            except:
                servic = Sersvice.objects.get(name_id=user.pk)
                mashins = Mashins.objects.filter(service_company=servic)
                print(mashins)
                for i in list(mashins):
                    yield TO.objects.filter(mashins_TO=i)
        else:
            return TO.objects.all()


class ComplaintListView(LoginRequiredMixin, ListView):
    permission_required = 'backend.view_complaint'
    model = Complaint
    template_name = 'backend/complaint/complaint_list.html'
    ordering = 'mashins_c'
    context_object_name = 'mashins_c'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = CustomUser.objects.get(pk=self.request.user.pk)

            try:
                clients = ClientG.objects.get(name_id=user.pk)
                mashins = Mashins.objects.filter(client=clients)
                for m in mashins:
                    yield Complaint.objects.filter(mashins_c=m)
            except:
                servic = Sersvice.objects.get(name_id=user)
                mashins = Mashins.objects.filter(service_company=servic)
                print(mashins)
                for i in list(mashins):
                    yield Complaint.objects.filter(mashins_c=i)
        else:
            return Complaint.objects.all()


class CarDetailView(LoginRequiredMixin, DetailView):
    permission_required = 'backend.view_car'
    model = Mashins
    template_name = 'backend/car/car_view.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CarCreateView(LoginRequiredMixin, CreateView):
    permission_required = 'backend.add_car'
    model = Mashins
    form_class = CarForm
    template_name = 'backend/car/car_create.html'
    success_url = reverse_lazy('car_list')


class CarUpdateView(LoginRequiredMixin, UpdateView):
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


class CarDeleteView(LoginRequiredMixin, DeleteView):
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


class MaintenanceCreateView(LoginRequiredMixin, CreateView):
    permission_required = 'backend.add_TO'
    model = TO
    form_class = MaintenanceForm
    template_name = 'backend/TO/maintenance_create.html'
    success_url = reverse_lazy('maintenance_list')


class MaintenanceUpdateView(LoginRequiredMixin, UpdateView):
    permission_required = 'backend.change_TO'
    model = TO
    form_class = MaintenanceForm
    template_name = 'backend/TO/maintenance_update.html'
    success_url = reverse_lazy('maintenance_list')


class MaintenanceDeleteView(LoginRequiredMixin, DeleteView):
    permission_required = 'backend.delete_TO'
    model = TO
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('maintenance_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vid_TO"] = 'maintenance'
        return context


class MaintenanceCarListView(LoginRequiredMixin, ListView):
    permission_required = 'backend.view_TO'
    model = TO
    template_name = 'backend/TO/maintenance_car.html'

    def get_queryset(self):
        car = Mashins.objects.get(pk=self.kwargs["pk"])
        return TO.objects.filter(mashins_TO=car)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = Mashins.objects.get(pk=self.kwargs["pk"])
        return context


class ComplaintCreateView(LoginRequiredMixin, CreateView):
    permission_required = 'backend.add_complaint'
    model = Complaint
    form_class = ComplaintForm
    template_name = 'backend/complaint/complaint_create.html'
    success_url = reverse_lazy('complaint_list')


class ComplaintUpdateView(LoginRequiredMixin, UpdateView):
    permission_required = 'backend.change_complaint'
    model = Complaint
    form_class = ComplaintForm
    template_name = 'backend/complaint/complaint_update.html'
    success_url = reverse_lazy('complaint_list')


class ComplaintDeleteView(LoginRequiredMixin, DeleteView):
    permission_required = 'backend.delete_complaint'
    model = Complaint
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('complaint_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'сomplaint'
        return context


class ComplaintCarListView(LoginRequiredMixin, ListView):
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
            context['atribute'] = maintenance.vid_TO
            context['description'] = maintenance.vid_TO.description
        elif atribute == 'service_TO':
            context['atribute'] = maintenance.service_TO
            context['description'] = maintenance.service_TO.description
        return context


class ComplaintDescriptionView(TemplateView):
    template_name = 'backend/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        complaint = Complaint.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'failure_node':
            context['atribute'] = complaint.failure_node
            context['description'] = complaint.failure_node.description
        elif atribute == 'recovery_method':
            context['atribute'] = complaint.recovery_method
            context['description'] = complaint.recovery_method.description
        elif atribute == 'mashins_c':
            context['atribute'] = complaint.mashins_c
            context['description'] = complaint.mashins_c.description
        elif atribute == 'service':
            context['atribute'] = complaint.service
            context['description'] = complaint.service.description
        return context


# API
class MaintenanceListAPI(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TOSerializer
    queryset = TO.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


class MaintenanceUserListAPI(generics.ListAPIView):
    serializer_class = TOSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


class MaintenanceDetailAPI(generics.RetrieveAPIView):
    serializer_class = TOSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = TO.objects.get(pk=self.kwargs['pk'])
        return obj


class ComplaintListAPI(generics.ListAPIView):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


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
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
