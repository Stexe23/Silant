from rest_framework import generics, viewsets
from rest_framework import permissions

from silant.backend.models import (ModMotorG, ModTransmissionG, Mashins, ModMashinsG, ModDriveBridgeG,
                                   ModControllBridgeG, RecoveryMethodG, Complaint, NatureRefusalG,
                                   ClientG, Sersvice, VidTOG, TO)
from serializers import (ModMotorGSerializer, ModTransmissionGSerializer, MashinsSerializer, ModMashinsGSerializer,
                         ModDriveBridgeGSerializer, ModControllBridgeGSerializer, RecoveryMethodGSerializer,
                         ComplaintSerializer, NatureRefusalGSerializer, ClientGSerializer, SersviceSerializer,
                         VidTOGSerializer, TOSerializer)



# Список моделей моторов
class ModMotorGListCreate(viewsets.ModelViewSet):
    model = ModMotorG
    queryset = ModMotorG.objects.all()
    serializer_class = ModMotorGSerializer


# Список моделей трансмиссий
class ModTransmissionGListCreate(viewsets.ModelViewSet):
    model = ModTransmissionG
    queryset = ModTransmissionG.objects.all()
    serializer_class = ModTransmissionGSerializer


# Список машин
class MashinsListCreate(viewsets.ModelViewSet):
    model = Mashins
    queryset = Mashins.objects.all()
    serializer_class = MashinsSerializer


# Список моделей машин
class ModMashinsGListCreate(viewsets.ModelViewSet):
    model = ModMashinsG
    queryset = ModMashinsG.objects.all()
    serializer_class = ModMashinsGSerializer


# Список моделей ведущего моста
class ModDriveBridgeGListCreate(viewsets.ModelViewSet):
    model = ModDriveBridgeG
    queryset = ModDriveBridgeG.objects.all()
    serializer_class = ModDriveBridgeGSerializer


# Список моделей управляемого моста
class ModControllBridgeGListCreate(viewsets.ModelViewSet):
    model = ModControllBridgeG
    queryset = ModControllBridgeG.objects.all()
    serializer_class = ModControllBridgeGSerializer


# Список способов восстановления
class RecoveryMethodGListCreate(viewsets.ModelViewSet):
    model = RecoveryMethodG
    queryset = RecoveryMethodG.objects.all()
    serializer_class = RecoveryMethodGSerializer


# Список клиентов
class ClientGListCreate(viewsets.ModelViewSet):
    model = ClientG
    queryset = ClientG.objects.all()
    serializer_class = ClientGSerializer


# Список рекламаций
class ComplaintListCreate(viewsets.ModelViewSet):
    model = Complaint
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer


# Список характера отказов
class NatureRefusalGListCreate(viewsets.ModelViewSet):
    model = NatureRefusalG
    queryset = NatureRefusalG.objects.all()
    serializer_class = NatureRefusalGSerializer


# Список видов ТО
class VidTOGListCreate(viewsets.ModelViewSet):
    model = VidTOG
    queryset = VidTOG.objects.all()
    serializer_class = VidTOGSerializer


# Список ТО
class TOListCreate(viewsets.ModelViewSet):
    model = TO
    queryset = TO.objects.all()
    serializer_class = TOSerializer


# Список сервисных компаний
class SersviceListCreate(viewsets.ModelViewSet):
    model = Sersvice
    queryset = Sersvice.objects.all()
    serializer_class = SersviceSerializer
    permission_classes = [IsAcc]




