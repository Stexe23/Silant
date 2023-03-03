from rest_framework import generics, viewsets
from rest_framework import permissions

from users.models import CustomUser, AbstractUser
from silant.backend.models import (ModMotorG, ModTransmissionG, Mashins, ModMashinsG, ModDriveBridgeG,
                                   ModControllBridgeG, RecoveryMethodG, Complaint, NatureRefusalG,
                                   ClientG, Sersvice, VidTOG, TO)
from serializers import (ModMotorGSerializer, ModTransmissionGSerializer, MashinsSerializer, ModMashinsGSerializer,
                         ModDriveBridgeGSerializer, ModControllBridgeGSerializer, RecoveryMethodGSerializer,
                         ComplaintSerializer, NatureRefusalGSerializer, ClientGSerializer, SersviceSerializer,
                         VidTOGSerializer, TOSerializer, AccountSerializer)


# Список моделей моторов
class ModMotorGListCreate(viewsets.ModelViewSet):
    queryset = ModMotorG.objects.all()
    serializer_class = ModMotorGSerializer


# Список моделей трансмиссий
class ModTransmissionGListCreate(viewsets.ModelViewSet):
    queryset = ModTransmissionG.objects.all()
    serializer_class = ModTransmissionGSerializer


# Список машин
class MashinsListCreate(viewsets.ModelViewSet):
    queryset = Mashins.objects.all()
    serializer_class = MashinsSerializer


# Список моделей машин
class ModMashinsGListCreate(viewsets.ModelViewSet):
    queryset = ModMashinsG.objects.all()
    serializer_class = ModMashinsGSerializer


# Список моделей ведущего моста
class ModDriveBridgeGListCreate(viewsets.ModelViewSet):
    queryset = ModDriveBridgeG.objects.all()
    serializer_class = ModDriveBridgeGSerializer


# Список моделей управляемого моста
class ModControllBridgeGListCreate(viewsets.ModelViewSet):
    queryset = ModControllBridgeG.objects.all()
    serializer_class = ModControllBridgeGSerializer


# Список способов восстановления
class RecoveryMethodGListCreate(viewsets.ModelViewSet):
    queryset = RecoveryMethodG.objects.all()
    serializer_class = RecoveryMethodGSerializer


# Список клиентов
class ClientGListCreate(viewsets.ModelViewSet):
    queryset = ClientG.objects.all()
    serializer_class = ClientGSerializer


# Список рекламаций
class ComplaintListCreate(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer


# Список характера отказов
class NatureRefusalGListCreate(viewsets.ModelViewSet):
    queryset = NatureRefusalG.objects.all()
    serializer_class = NatureRefusalGSerializer


# Список видов ТО
class VidTOGListCreate(viewsets.ModelViewSet):
    queryset = VidTOG.objects.all()
    serializer_class = VidTOGSerializer


# Список ТО
class TOListCreate(viewsets.ModelViewSet):
    queryset = TO.objects.all()
    serializer_class = TOSerializer


# Список сервисных компаний
class SersviceListCreate(viewsets.ModelViewSet):
    queryset = Sersvice.objects.all()
    serializer_class = SersviceSerializer
    permission_classes = []


class AccountListCreate(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = AccountSerializer




