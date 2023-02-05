from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from .models import (ModMotorG, ModTransmissionG, Mashins, ModMashinsG, ModDriveBridgeG,
                     ModControllBridgeG, RecoveryMethodG, Complaint, UsersSilant, NatureRefusalG,
                     ClientG, Sersvice, VidTOG, TO)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# Список моделей моторов
class ModMotorGList(ListView):
    model = ModMotorG
    ordering = 'model_motor'


# Список моделей трансмиссий
class ModTransmissionGList(ListView):
    model = ModTransmissionG
    ordering = 'model_transmission'


# Список машин
class MashinsList(ListView):
    model = Mashins
    ordering = 'zav_nom_mashins'


# Список моделей машин
class ModMashinsGList(ListView):
    model = ModMashinsG
    ordering = 'model_mashins'


# Список моделей ведущего моста
class ModDriveBridgeGList(ListView):
    model = ModDriveBridgeG
    ordering = 'model_drive_bridge'


# Список моделей управляемого моста
class ModControllBridgeGList(ListView):
    model = ModControllBridgeG
    ordering = 'model_controll_bridge'


# Список способов восстановления
class RecoveryMethodGList(ListView):
    model = RecoveryMethodG
    ordering = 'recovery_method'


# Список клиентов
class ClientGList(ListView):
    model = ClientG
    ordering = 'client'


# Список рекламаций
class ComplaintList(ListView):
    model = Complaint
    ordering = 'reason_refusal'


# Список характера отказов
class NatureRefusalGList(ListView):
    model = NatureRefusalG
    ordering = 'reason_refusal'


# Список видов ТО
class VidTOGList(ListView):
    model = VidTOG
    ordering = 'vid_TO'


# Список ТО
class TOList(ListView):
    model = TO
    ordering = 'vid_TO'


# Список сервисных компаний
class SersviceList(ListView):
    model = Sersvice
    ordering = 'service_company'


# Список пользователей
class UsersSilantList(ListView):
    model = UsersSilant
    ordering = 'name'
